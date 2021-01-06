#!/usr/bin/env python3
'''
This module contains one function: safely_get_value()
It uses type annotation.
'''

from typing import Mapping, Any, Union, TypeVar



def safely_get_value(dct: Mapping, key: Any, default: Union[TypeVar('T'), None] = None) -> Union[Any, TypeVar('T')]:
    '''return a complex annotated type'''
    if k in dct:
        return dct[k]
    else:
        return default
