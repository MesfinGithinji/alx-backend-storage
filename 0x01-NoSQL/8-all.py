#!/usr/bin/env python3
"""
Function to List all documents
"""


def list_all(mongo_collection):
    """
    lists all documents in a collection

    :param mongo_collection:
    :return documents
    """
    documents = mongo_collection.find()
    return documents

