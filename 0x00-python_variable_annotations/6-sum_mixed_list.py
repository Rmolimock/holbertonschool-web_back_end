#!/usr/bin/env python3
'''
This module contains one function: sum_mixed_list()
It uses type annotation.
'''

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''return the sum of a given list of floats and ints'''
    ret = 0.0
    for i in mxd_lst:
        ret += i
    return ret
