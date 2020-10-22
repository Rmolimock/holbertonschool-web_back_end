#!/usr/bin/env python3

"""async comprehension"""

from typing import List
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ 10 random numbers """
    return [n async for n in async_generator()]
