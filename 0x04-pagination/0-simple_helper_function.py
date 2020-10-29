#!/usr/bin/env python3

""" helper function """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ range of indexes read on 'page' in a file """
    return ((page - 1) * page_size, page * page_size)
