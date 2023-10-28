
"""
Least Recently Used (LRU)
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class
    """
    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Inputs the keys in the queue
        """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard = self.queue.pop(0)
                del self.cache_data[discard]
                print(f'DISCARD: {discard}')
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve items from the cache
        """
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None
