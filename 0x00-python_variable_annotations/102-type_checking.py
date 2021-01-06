#!/usr/bin/env python3
'''
This module contains one function: zoom_array()
It uses type annotation.
'''

from typing import Any, List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ zoom array function for holberton project """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), int(3.0))
