#!/usr/bin/env python3

"""
basic async generator
"""


from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """random number from 0 to 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
