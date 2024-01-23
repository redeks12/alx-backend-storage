#!/usr/bin/env python3
"""0x01. NoSQL"""


def list_all(mongo_collection):
    """
    Prototype: def list_all(mongo_collection)
    Return an empty list if no document in the collection
    """
    cursur = mongo_collection.find()
    return cursur
