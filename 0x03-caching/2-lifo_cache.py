#!/usr/bin/python3
""" LIFOCache puts and gets data into a cache """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ puts and gets items into a cache in LIFO order """

    def __init__(self):
        """ inherit from parent and init keys """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ put a new item into the cash """
        if item is not None and key is not None:
            self.cache_data[key] = item
            if key in self.keys:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            else:
                self.keys.append(key)
            if BaseCaching.MAX_ITEMS < len(self.keys):
                discarded = self.keys.pop(len(self.keys) - 2)
                del self.cache_data[discarded]
                print(f"DISCARD: {discarded}")

    def get(self, key):
        """ get an item from the cache """
        if key not in self.cache_data or not key:
            return None
        return self.cache_data[key]
