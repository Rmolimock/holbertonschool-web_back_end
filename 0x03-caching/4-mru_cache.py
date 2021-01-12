#!/usr/bin/python3
""" MRU Cache class docstring for holberton checker """

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRU Cache class docstring for holberton checker
    """

    def __init__(self):
        """ MRU Cache class docstring for holberton checker
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ MRU Cache class docstring for holberton checker
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

            if key in self.keys:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            else:
                self.keys.append(key)

            if BaseCaching.MAX_ITEMS < len(self.keys):
                i = self.keys.pop(len(self.keys) - 2)
                del self.cache_data[i]
                print(f"DISCARD: {i}")

    def get(self, key):
        """ MRU Cache class docstring for holberton checker
        """
        if not key or key not in self.cache_data:
            return None
        self.keys.append(self.keys.pop(self.keys.index(key)))
        return self.cache_data[key]
