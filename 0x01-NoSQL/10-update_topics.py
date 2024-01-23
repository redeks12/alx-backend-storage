#!/usr/bin/env python3
"""0x01. NoSQL"""


def update_topics(mongo_collection, name, topics):
    """Write a Python function that changes all topics of a school document based on the name:"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
