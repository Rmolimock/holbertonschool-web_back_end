#!/usr/bin/env python3
"""
hyper pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """ server class
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            # dict of {line number: line} in dataset
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ comment """
        assert type(page_size) == int
        assert type(index) == int
        assert index > 0
        size = len(self.indexed_dataset())
        assert index < size
        data, k = [], index
        for _ in range(page_size):
            while not self.indexed_dataset().get(k):
                k += 1
            data.append([self.indexed_dataset().get(k)])
            k += 1
        return {
            "index": index,
            "next_index": k,
            "page_size": page_size,
            "data": data
        }
