#!/usr/bin/env python3
'''
This module contains one function: element_length()
It uses type annotation.
'''

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''return list of tuples containing Sequence and int'''
    return [(k, len(k)) for k in lst]
