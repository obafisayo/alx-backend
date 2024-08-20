#!/usr/bin/env python3
'''
    index_range
'''
from typing import Tuple


def index_range(page, page_size) -> Tuple[int, int]:
    """Retrieves the index from a given page and page size
    
    Keyword arguments:
    page -- the page to be located
    page_size -- the size of the page
    Return: a tuple of the start index and end index.
    """
    