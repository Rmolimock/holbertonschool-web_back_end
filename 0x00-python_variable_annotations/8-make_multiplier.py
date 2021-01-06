#!/usr/bin/env python3
'''
This module contains one function: make_multiplier()
It uses type annotation.
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''return a function to multiply numbers by a given multiplier'''
    return lambda f: f * multiplier
