#!/usr/bin/env python3
"""
Simple pagination module.

This module provides a `Server` class to handle pagination for a dataset
of popular baby names stored in a CSV file. It includes methods to cache
the dataset and retrieve specific pages of data.

Functions:
    - index_range: Calculates the start and end indices for a given page
      and page size.

Classes:
    - Server: Handles dataset caching and pagination.
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for a given page and page size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index (inclusive)
        and the end index (exclusive).
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """
    Server class to paginate a database of popular baby names.

    Attributes:
        DATA_FILE (str): The name of the CSV file containing the dataset.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the Server instance.

        Attributes:
            __dataset (List[List] or None): Cached dataset loaded from
            the CSV file.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache the dataset from the CSV file.

        If the dataset is already cached, it returns the cached version.

        Returns:
            List[List]: The dataset as a list of rows,
            excluding the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a page of the dataset.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows corresponding to the requested page.
            If the page is out of range, an empty list is returned.

        Raises:
            AssertionError: If `page` or `page_size` are not positive integers.
        """
        # Validate arguments
        assert isinstance(page, int) and page > 0, \
            "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive integer"

        # Get the dataset
        dataset = self.dataset()

        # Use index_range to find the correct indices
        start, end = index_range(page, page_size)

        # Return the appropriate page, or an empty list
        if start >= len(dataset):
            return []

        return dataset[start:end]
