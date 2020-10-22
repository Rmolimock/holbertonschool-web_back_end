#!/usr/bin/env python3
""" parallel comprehension """

import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ time of four coroutines """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for n in range(4)))
    return time.perf_counter() - start
