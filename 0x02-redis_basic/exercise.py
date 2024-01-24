#!/usr/bin/env python3
"""0x02. Redis basic"""

from functools import wraps
from typing import Any, Callable, Union
from uuid import uuid4

import redis


def count_calls(func: Callable) -> Callable:
    """decorator for counting calls"""

    @wraps(func)
    def wrapper(self, *args, **kwargs) -> str:
        """adds a new call to the db"""
        self._redis.incr(func.__qualname__)
        return func(self, *args, **kwargs)

    return wrapper


def call_history(func: Callable) -> Callable:
    """decorator for counting calls"""

    @wraps(func)
    def wrapper(self, *args, **kwargs) -> str:
        """adds a new call to the db"""
        outputs = f"{func.__qualname__}:outputs"
        inputs = f"{func.__qualname__}:inputs"
        self._redis.rpush(inputs, str(args))
        key = func(self, *args, **kwargs)
        self._redis.rpush(outputs, str(key))
        return key

    return wrapper


def replay(func: Callable) -> None:
    """In this tasks, we will implement a replay
    function to display the history of calls of a particular function."""
    _redis = redis.Redis()
    outputs = _redis.lrange(f"{func.__qualname__}:outputs", 0, -1)
    inputs = _redis.lrange(f"{func.__qualname__}:inputs", 0, -1)
    print(f"{func.__qualname__} was called {len(outputs)} times")
    for i, o in zip(inputs, outputs):
        print(f"{func.__qualname__}(*{i.decode('utf-8')}) -> {o.decode('utf-8')}")


class Cache:
    """Cache implementation"""

    def __init__(self) -> None:
        """initialize the cache  object"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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


cache = Cache()
cache.store("foo")
cache.store("bar")
cache.store(42)
replay(cache.store)
