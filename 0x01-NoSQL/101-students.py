#!/usr/bin/env python3
"""0x01. NoSQL"""

list_all = __import__("8-all").list_all


def top_students(mongo_collection):
    """Write a Python function that returns all students sorted by average score"""
    arrs = mongo_collection.find()
    news = []
    for i in arrs:
        bb = 0
        for a in i.get("topics"):
            bb += a.get("score")

        i["averageScore"] = bb / 3
        news.append(i)
    return sorted(news, key=lambda x: x["averageScore"], reverse=True)
