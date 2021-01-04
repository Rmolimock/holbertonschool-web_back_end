#!/usr/bin/python3
""" BasicCache puts and gets data into a cache """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache puts and gets items into a cache """
    def put(self, key, item):
        """ put a new item into the cash """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ get an item from the cache """
        if key not in self.cache_data or not key:
            return None
        return self.cache_data[key]
