#!/usr/bin/python3
""" LRU Cache class docstring for holberton checker """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU Cache class docstring for holberton checker
    """

    def __init__(self):
        """ LRU Cache class docstring for holberton checker
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ LRU Cache class docstring for holberton checker
        """
        if item is not None and key is not None:
            self.cache_data[key] = item

        if key in self.keys:
            self.keys.append(self.keys.pop(self.keys.index(key)))
        else:
            self.keys.append(key)

            if BaseCaching.MAX_ITEMS < len(self.keys):
                i = self.keys.pop(0)
                del self.cache_data[i]
                print(f"DISCARD: {:i}")

    def get(self, key):
        """ LRU Cache class docstring for holberton checker
        """
        if not key or key not in self.cache_data:
            return None
        self.keys.append(self.keys.pop(self.keys.index(key)))
        return self.cache_data[key]
