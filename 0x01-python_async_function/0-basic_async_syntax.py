#!/usr/bin/env python3

"""
a simple coroutine
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    simple coroutine
    """
    r = random.random() * max_delay
    await asyncio.sleep(r)
    return r