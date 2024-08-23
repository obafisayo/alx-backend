#!/usr/bin/env python3
"""A cache system implementing the FIFO cache replacement policy
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """Implements the FIFO cache replacement policy"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds item to the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            deleted_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD: {}".format(deleted_key))

    def get(self, key):
        """Gets the item of the key"""
        if key is None:
            return
        if key not in self.cache_data:
            return
        return (self.cache_data.get(key, None))
