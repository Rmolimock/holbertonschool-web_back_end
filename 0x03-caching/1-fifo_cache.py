#!/usr/bin/python3
""" FIFO """

from queue import Queue

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache
    """
    def __init__(self):
        """ init """
        super().__init__()
        self.q = Queue()

    def put(self, key: str, item: str):
        """ put """
        if not key or not item:
            return
        if key not in self.cache_data:
            self.q.put(key)
        self.cache_data[key] = item
        if BaseCaching.MAX_ITEMS < self.q.qsize():
            key_removed = self.q.get()
            del self.cache_data[key_removed]
            print("DISCARD: {}".format(key_removed))

    def get(self, key: str) -> str:
        """ get cache data from self.cache_data """
        return self.cache_data[key] if key in self.cache_data else None
