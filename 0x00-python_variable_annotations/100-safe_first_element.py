#!/usr/bin/env python3
'''
This module contains one function: safe_first_element()
It uses type annotation.
'''

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''return the first element in a given sequence'''
    if lst:
        return lst[0]
    else:
        return None
