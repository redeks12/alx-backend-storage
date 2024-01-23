#!/usr/bin/env python3
"""0x01. NoSQL"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print(f"{db.count_documents({})} logs")
    print("Methods:")
    [print(f"\tmethod {val}: {db.count_documents({'method': val})}") for val in methods]
    print(f"{db.count_documents({'method': 'GET', 'path': '/status'})} status check")
    schema = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {"_id": 0, "ip": "$_id", "count": 1}},
    ]
    [print("\t{}: {}".format(i["ip"], i["count"])) for i in db.aggregate(schema)]
