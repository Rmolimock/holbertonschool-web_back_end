#!/usr/bin/env python3
'''
This module contains one function: sum_list()
It uses type annotation.
'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''This function returns the sum of a given list of floats'''
    ret = 0
    for i in input_list:
        ret += i
    return ret
