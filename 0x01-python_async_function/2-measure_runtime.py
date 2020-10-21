#!/usr/bin/env python3

"""get execution time"""

import asyncio
from time import perf_counter
import random

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """get execution time"""
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    t = perf_counter() - i
    return t