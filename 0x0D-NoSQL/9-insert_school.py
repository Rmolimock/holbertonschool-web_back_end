#!/usr/bin/env python3
""" insert a document into a collection with pymongo """


def insert_school(mongo_collection, **kwargs):
    """ insert a document into a collection with pymongo """
    return mongo_collection.insert_one(kwargs).inserted_id
