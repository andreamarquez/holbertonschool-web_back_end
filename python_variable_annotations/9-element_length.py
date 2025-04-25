#!/usr/bin/env python3
"""
This module provides a function to calculate the
length of elements in an iterable.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in an iterable of sequences.

    Args:
        lst (Iterable[Sequence]): An iterable containing
        sequences (e.g., strings, lists).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where
        each tuple contains a sequence and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
