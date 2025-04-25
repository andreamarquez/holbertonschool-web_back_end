#!/usr/bin/env python3
"""
This module provides a function to create a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float and
        returns the result of multiplying it by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiply the given value by the multiplier.

        Args:
            value (float): The value to be multiplied.

        Returns:
            float: The result of the multiplication.
        """
        return value * multiplier

    return multiplier_function
