#!/usr/bin/env python3
""" track how many times a particular URL was accessed in a key """
import requests
from redis.client import Redis
from typing import Callable
from functools import wraps


r = Redis()


def count(name: Callable) -> Callable:
    """ count """
    n = str(name)
    @wraps(n)
    def wrapper(self, *args, **kwargs):
        """ wrapper function """
        r.incr(n)
        r.setex(n, 10, r.get(n))
    return wrapper


def get_page(url: str) -> str:
    """ get page """
    key = f"count:{url}"
    @count
    def request_page(key: str, url: str) -> str:
        """ request_page """
        return requests.get(url).text

    return request_page(key, url)


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
