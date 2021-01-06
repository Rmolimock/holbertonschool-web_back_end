#!/usr/bin/env python3
'''
This module contains one function: safely_get_value()
It uses type annotation.
'''

from typing import Mapping, Any, Union, TypeVar


U1 = Union[TypeVar('T'), None]
U2 = Union[Any, TypeVar('T')]


def safely_get_value(dct: Mapping, key: Any, default: U1 = None) -> U2:
    '''return a complex annotated type'''
    if k in dct:
        return dct[k]
    else:
        return default
