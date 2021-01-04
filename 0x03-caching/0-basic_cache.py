#!/usr/bin/python3
""" BasicCache """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache """
    def put(self, key, item):
        """ put """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ get """
        if key not in self.cache_data or not key:
            return None
        return self.cache_data[key]
