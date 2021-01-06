#!/usr/bin/env python3
'''
This module contains one function: to_kv()
It uses type annotation.
'''

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ this function takes a string and returns a tuple """
    return (k, v**2)
