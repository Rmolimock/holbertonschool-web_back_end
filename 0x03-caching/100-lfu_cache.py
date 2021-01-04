#!/usr/bin/python3
""" LFUCache puts and gets data into a cache """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ puts and gets items into a cache in LFU order """

    def __init__(self):
        self.counter = 0
        self.used = {}
        self.ages = {}
        super().__init__()

    def count_used(self, key):
        """ count the number of keys """
        if key not in self.used:
            self.used[key] = 1
        else:
            self.used[key] += 1

    def put(self, key, item):
        """ put a new item into the cash """
        if key and item:
            self.cache_data[key] = item
            if BaseCaching.MAX_ITEMS < len(self.cache_data):
                least = min(self.used.values())
                for i, _ in sorted(self.ages.items(), key=lambda n: n[1]):
                    if self.used[i] == least:
                        self.cache_data.pop(i)
                        self.used.pop(i)
                        self.ages.pop(i)
                        break
                print('DISCARD:', i)
            self.count_used(key)
            self.ages[key] = self.counter
            self.counter += 1

    def get(self, key):
        """ get an item from the cache """
        if key in self.cache_data and key:
            self.ages[key] = self.counter
            self.count_used(key)
            self.counter += 1
            return self.cache_data.get(key)
        return None
