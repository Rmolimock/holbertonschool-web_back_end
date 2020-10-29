#!/usr/bin/env python3
""" simple pagination
"""

import csv
import math
from typing import List, Tuple


class Server:
    """ server class
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ return page number
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        start, stop = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        if stop > len(data):
            stop = len(data)
        return data[start:stop]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ range of indexes """
    return ((page - 1) * page_size, page * page_size)