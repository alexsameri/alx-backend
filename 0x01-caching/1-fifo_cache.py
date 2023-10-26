#!/usr/bin/env python3
"""module 1
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    MAX_ITEMS: maximum number of items
    """
    def __init__(self):
        """ Instantiation method, sets instance attributes
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        len of the items
        """
        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            keyout = self.cache_data.popitem(last=False)
            print(f"DISCARD: {keyout}")

        self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key
        Args:
            key: the key r=to retrieve the value for
        Returns:
            The value associated with the key in the cache,
            or None if the key doesn't exist
        """
        return self.cache_data.get(key, None)
