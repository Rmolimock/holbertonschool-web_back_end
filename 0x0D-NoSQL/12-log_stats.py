#!/usr/bin/env python3
""" nginx logs in mongoDB """
from pymongo import MongoClient


def log_info(log):
    """ nginx logs in mongoDB """
    print("{} logs".format(log.estimated_document_count()))
    print("Methods:")
    print("\tmethod GET: {}".format(log.count_documents({"method": "GET"})))
    print("\tmethod POST: {}".format(log.count_documents({"method": "POST"})))
    print("\tmethod PUT: {}".format(log.count_documents({"method": "PUT"})))
    print("\tmethod PATCH: {}".format(log.count_documents(
         {"method": "PATCH"})))
    print("\tmethod DELETE: {}".format(log.count_documents(
         {"method": "DELETE"})))
    print("{} status check".format(log.count_documents({"path": "/status"})))


if __name__ == "__main__":
    """ main """
    c = MongoClient('mongodb://127.0.0.1:27017')
    log = c.logs.nginx
    log_info(log)
