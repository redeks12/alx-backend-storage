#!/usr/bin/env python3
"""0x01. NoSQL"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    school_collection = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("{} logs".format(school_collection.count_documents({})))
    print("Methods:")
    [
        print(
            "\tmethod {}: {}".format(
                val, school_collection.count_documents({"method": val})
            )
        )
        for val in methods
    ]
    print(
        "{} status check".format(school_collection.count_documents({"path": "/status"}))
    )
