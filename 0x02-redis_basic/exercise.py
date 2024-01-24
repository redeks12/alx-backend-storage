#!/usr/bin/env python3
"""0x02. Redis basic"""

from typing import Union
from uuid import uuid4

import redis


class Cache:
    """Cache implementation"""

    def __init__(self) -> None:
        """initialize the cache  object"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, bytes, float]) -> str:
        """Writing strings to Redis"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
