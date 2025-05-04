#!/usr/bin/env python3
"""
This module provides a function to insert a new document into a MongoDB collection.
"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        **kwargs: Key-value pairs representing the fields and values of the document to insert.

    Returns:
        ObjectId: The ID of the newly inserted document.
    """
    if mongo_collection is None:
        return None
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
