#!/usr/bin/env python
"""A cache system implementing the FIFO cache replacement policy
"""
from base_caching import BaseCaching
from collections import deque


class LIFOCache(BaseCaching):
    """Implements the LIFO cache replacement policy"""
    def __init__(self):
        super().__init__()
        self.cache_data = deque()

    def put(self, key, item):
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.remove(key)
        self.cache_data.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            deleted_key, _ = self.cache_data.popleft()
            print("DISCARD: ", deleted_key)

    def get(self, key):
        """Gets the item of the key"""
        if key is None:
            return
        if key not in self.cache_data:
            return
        return (self.cache_data.get(key, None))
