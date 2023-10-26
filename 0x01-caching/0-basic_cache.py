#!/usr/bin/env python3
"""Caching inheritance
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ uses a dictionary to sort out data
    """
    def put(self, key, item):
        """
        assign to the dict self.cache_data
        the item valur for the key
        """
        if item is not None and key is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        must return the value in self.cache_data
        linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key, None)
