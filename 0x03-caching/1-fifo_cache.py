#!/usr/bin/python3
""" FIFOCACHE puts and gets data into a cache """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ puts and gets items into a cache in FIFO order """

    def __init__(self):
        """ inherit from parent and init keys """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ put a new item into the cash """
        if item is not None and key is not None:
            self.cache_data[key] = item
            if not key in self.keys:
                self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discarded = self.keys.pop(0)
                del self.cache_data[discarded]
                print(f"DISCARD: {discarded}")

    def get(self, key):
        """ get an item from the cache """
        if not key in self.cache_data or not key:
            return None
        return self.cache_data[key]
