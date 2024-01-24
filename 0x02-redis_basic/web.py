#!/usr/bin/env python3
"""0x02. Redis basic"""

from functools import wraps
from typing import Callable

import requests
from redis import Redis


def count(func: Callable) -> Callable:
    """Count the number of times a callable"""

    @wraps(func)
    def wrapper(url: str) -> str:
        """Count the number of times a"""
        red = Redis()
        red.incr(f"count:{url}")
        cached_page = red.get(url)
        if cached_page:
            return cached_page.decode("utf-8")
        res = func(url)
        red.set(url, res, 10)

        return res

    return wrapper


def get_page(url: str) -> str:
    """Implementing an expiring web cache and tracker"""

    response = requests.get(url)
    return response.text


get_page("http://slowwly.robertomurray.co.uk")

red = Redis()
print(red.get("count:http://slowwly.robertomurray.co.uk"))
