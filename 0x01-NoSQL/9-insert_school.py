#!/usr/bin/env python3
"""0x01. NoSQL"""


def insert_school(mongo_collection, **kwargs):
    """Write a Python function that inserts a new document in a collection based on kwargs"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
