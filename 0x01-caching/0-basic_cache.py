#!/usr/bin/env python3
"""Caching inheritance
"""
from Base_Caching import BaseCaching


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
        return self.cache_data.get(key, None)
