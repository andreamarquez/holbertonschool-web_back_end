#!/usr/bin/env python3
"""
This module provides a function to calculate the sum of a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floating-point numbers.

    Args:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of the numbers in the list.
    """
    return sum(input_list)
