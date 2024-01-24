#!/usr/bin/env python3
"""0x02. Redis basic"""

from typing import Union
from uuid import uuid4

import redis


class Cache:
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, bytes, float]) -> str:
        key = str(uuid4())
        self._redis.set(key, data)
        return key
