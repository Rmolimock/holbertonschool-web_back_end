#!/usr/bin/python3
""" LIFO """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO """

    def __init__(self):
        """ init """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ put """
        if item is not None and key is not None:
            self.cache_data[key] = item
            if key in self.keys:
                self.keys.append(self.keys.pop(self.keys.index(key))) \
            else:
                self.keys.append(key)
            if BaseCaching.MAX_ITEMS < len(self.keys):
                discarded = self.keys.pop(len(self.keys) - 2)
                del self.cache_data[discarded]
                print(f"DISCARD: {discarded}")

    def get(self, key):
        """ get """
        if not key in self.cache_data or not key:
            return None
        return self.cache_data[key]
