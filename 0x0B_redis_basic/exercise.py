#!/usr/bin/env python3
""" redis basics """

import redis
from typing import Callable, Union, Optional
from functools import wraps
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """ count calls """
    n = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(n)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ call history """
    out = method.__qualname__ + ":outputs"
    in = method.__qualname__ + ":inputs"
    @wraps(method)
    def wrapper(self, *args):
        self._redis.rpush(in, str(args))
        res = method(self, *args)
        self._redis.rpush(out, str(res))
        return res
    return wrapper


def replay(method: Callable) -> str:
    """ relay """
    r = redis.Redis()
    n = Cache.store.__qualname__
    outputs = r.lrange("{}:outputs".format(n), 0, -1).decode("utf-8")
    inputs = r.lrange("{}:inputs".format(n), 0, -1).decode("utf-8")
    print(f"{n} was called {len(outputs)} times:")
    for in, out in tuple(zip(inputs, outputs)):
        print(f"{n}(*('{in}',)) -> {out}")


class Cache():
    """ Cache """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store redis data """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ get redis data """
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, data: bytes) -> str:
        """ decode bytes """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """ bytes to int """
        from os import sys
        return int.from_bytes(data, sys.byteorder)
