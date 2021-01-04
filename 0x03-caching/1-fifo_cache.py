#!/usr/bin/python3
""" FIFOCache """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO """

    def __init__(self):
        """ Init """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ put """
        if item is not None and key is not None:
            self.cache_data[key] = item
            if not key in self.keys:
                self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discarded = self.keys.pop(0)
                del self.cache_data[discarded]
                print(f"DISCARD: {discarded}")

    def get(self, key):
        """ get"""
        if not key in self.cache_data or not key:
            return None
        return self.cache_data[key]
