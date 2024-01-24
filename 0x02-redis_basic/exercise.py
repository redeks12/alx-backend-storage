#!/usr/bin/env python3
"""0x02. Redis basic"""

from typing import Callable, Union
from uuid import uuid4
from functools import wraps
import redis


def count_calls(func: Callable) -> Callable:
    @wraps(func)
    def ans(*args, **kwargs):
        val = args[0]
        val._redis.incr(func.__qualname__)
        return func(*args, **kwargs)

    return ans


class Cache:
    """Cache implementation"""

    def __init__(self) -> None:
        """initialize the cache  object"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, int, bytes, float]) -> str:
        """Writing strings to Redis"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: Union[str, int, bytes, float], fn: Callable = None
    ) -> Union[str, int]:
        """Reading from Redis and recovering original type"""
        data = self._redis.get(key)
        if data is not None and callable(fn):
            data = fn(data)

        return data

    def get_str(self, val):
        """Reading from Redis and recovering original type"""
        return self.get(val, fn=lambda x: x.decode("utf-8") if x else None)

    def get_int(self, key):
        # Use get method with int conversion function
        return self.get(key, fn=lambda x: int(x) if x else None)
