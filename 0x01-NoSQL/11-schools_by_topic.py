#!/usr/bin/env python3
"""0x01. NoSQL"""


def schools_by_topic(mongo_collection, topic):
    """Write a Python function that returns the list of school having a specific topic:"""
    val = mongo_collection.find({"topics": topic})
    return val
