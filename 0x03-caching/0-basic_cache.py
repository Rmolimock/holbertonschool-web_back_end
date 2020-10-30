#!/usr/bin/python3
""" basic cahing """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache
    """
    def put(self, key: str, item: str):
        """ put """
        if key and item:
            self.cache_data[key] = item

    def get(self, key: str) -> str:
        """ get """
        return self.cache_data[key] if key in self.cache_data else None
