
"""
Least Frequently Used Cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LRU Cahe
    """
    def __init__(self):
        super().__init__()
        self.keys = []
    def put(self, key, item):
        """
        insert the keys
        """
        if key is None or item is None:
            return
        if key in self.keys:
            self.keys.remove(key)
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru = self.keys.pop()
            del self.cache_data[lru]
            print(f"DISCARD: {lru}")
        self.keys.insert(0, key)
        self.cache_data[key] = item
    def get(self, key):
        """
        Retrieve items from the cache
        """
        if key is None:
            return None
        if key in self.keys:
            self.keys.remove(key)
            self.keys.insert(0, key)
        return self.cache_data.get(key, None)
