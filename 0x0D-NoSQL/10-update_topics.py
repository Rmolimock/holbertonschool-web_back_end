#!/usr/bin/env python3
""" update values in every matching document """


def update_topics(mongo_collection, name, topics):
    """ update values in every matching document """
    return (mongo_collection.update_many({"name": name},
                                         {"$set": {"topics": topics}}
                                         ))
