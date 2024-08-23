#!/usr/bin/env python3
"""A basic caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A basic caching system that inherits from the superclass basecaching
    """
    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        if key is None:
            return
        if key not in self.cache_data:
            return
        return (self.cache_data.get(key, None))
