#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination module.

This module provides a `Server` class to handle pagination for a dataset
of popular baby names stored in a CSV file. It includes methods to cache
the dataset, retrieve specific pages of data, and provide deletion-resilient
hypermedia-style pagination.

Functions:
    - indexed_dataset: Returns the dataset indexed by position.
    - get_hyper_index: Retrieves a page of data starting at a given index,
      ensuring resilience to deletions in the dataset.

Classes:
    - Server: Handles dataset caching, pagination, and deletion-resilient
      hypermedia pagination.
"""

import csv
import math
from typing import List, Dict


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
            __dataset (List[List] or None): Cached dataset loaded
            from the CSV file.
            __indexed_dataset (Dict[int, List] or None): Indexed
            version of the dataset.
        """
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Create and cache an indexed version of the dataset.

        The dataset is indexed by its position, starting at 0. Only the first
        1000 rows of the dataset are included in the indexed version.

        Returns:
            Dict[int, List]: A dictionary where keys are indices and values
            are rows of the dataset.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: truncated_dataset[i] for i in range(len(truncated_dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve a page of data starting at the given index.

        This method ensures resilience to deletions in the dataset by skipping
        missing indices and continuing to retrieve data until the requested
        page size is met.

        Args:
            index (int): The starting index for the page.
            page_size (int): The number of items to include in the page.

        Returns:
            Dict: A dictionary containing the following keys:
                - index (int): The starting index of the page.
                - next_index (int): The index to start the next page.
                - page_size (int): The number of items on the current page.
                - data (List[List]): The data for the current page.

        Raises:
            AssertionError: If `index` is None or out of range.
        """
        # Validate the index
        assert index is not None and 0 <= index < len(self.indexed_dataset())

        data = []
        current_idx = index
        dataset = self.indexed_dataset()

        # Collect data while skipping missing indices
        while len(data) < page_size and current_idx < len(dataset) + page_size:
            if current_idx in dataset:
                data.append(dataset[current_idx])
            current_idx += 1

        return {
            "index": index,
            "next_index": current_idx,
            "page_size": len(data),
            "data": data
        }
