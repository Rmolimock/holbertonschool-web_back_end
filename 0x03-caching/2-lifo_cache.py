#!/usr/bin/python3
""" LIFO """

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache
    """
    def __init__(self):
        """ initiate instance variable """
        super().__init__()
        self.last = ''

    def put(self, key: str, item: str):
        """ put """
        if key and item:
            self.cache_data[key] = item
        if BaseCaching.MAX_ITEMS < len(self.cache_data):
            self.cache_data.pop(self.last)
            print('DISCARD:', self.last)
        if key:
            self.last = key

    def get(self, key: str) -> str:
        """ get """
        return self.cache_data[key] if key in self.cache_data else None
