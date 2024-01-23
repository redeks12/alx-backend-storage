#!/usr/bin/env python3
"""0x01. NoSQL"""


def insert_school(mongo_collection, **kwargs):
    """Write a Python function that inserts a new document in a collection based on kwargs"""
    mongo_collection.insert_one(kwargs)
