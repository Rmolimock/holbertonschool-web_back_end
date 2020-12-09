#!/usr/bin/env python3
""" list all documents in a collection with pymongo """


def list_all(mongo_collection):
    """ llist all documents in a collection with pymongo """
    return [doc for doc in mongo_collection.find()]
