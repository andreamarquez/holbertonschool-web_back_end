#!/usr/bin/env python3
"""
This module provides a function to find schools by a specific topic in a MongoDB collection.
"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        topic (str): The topic to search for.

    Returns:
        list: A list of schools (documents) that have the specified topic.
    """
    return list(mongo_collection.find({"topics": topic}))
