#!/usr/bin/env python3
"""
This module provides a function to list all documents in a MongoDB collection.
"""

import pymongo


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.

    Returns:
        list: A list of all documents in the collection. If the collection is empty
              or the collection object is invalid, an empty list is returned.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
