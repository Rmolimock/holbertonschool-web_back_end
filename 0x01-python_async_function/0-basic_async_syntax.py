#!usr/bin/env python3
""" simple coroutine """

import asyncio


async def wait_random(max_delay = 10):
    """ simple coroutine """
    import random
    r = random.randint(0, max_delay - 1)
    await asyncio.sleep(r)
    return r