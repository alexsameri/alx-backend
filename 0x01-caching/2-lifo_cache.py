#!/usr/bin/env python3
"""
Last in, first out
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    inherits from Base_Caching
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        discard the last item
        """
        if key is not None or item is not None:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                key_out = list(self.cache_data.keys())[-1]
                print(f"DISCARD: {key_out}")
                del self.cache_data[key_out]

        self.cache_data[key] = item

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        """
        return self.cache_data.get(key, None)
