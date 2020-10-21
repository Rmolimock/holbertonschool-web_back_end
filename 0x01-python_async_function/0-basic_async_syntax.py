#!usr/bin/env python3
""" simple coroutine """

import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ simple coroutine """
    import random
    r = random.random() * max_delay
    await asyncio.sleep(r)
    return r