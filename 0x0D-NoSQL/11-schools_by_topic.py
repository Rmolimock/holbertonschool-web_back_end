#!/usr/bin/env python3
""" documents with matching value with pymongo """


def schools_by_topic(mongo_collection, topic):
    """ documents with matching value with pymongo """
    return mongo_collection.find({"topics": topic})
