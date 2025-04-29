#!/usr/bin/env python3
"""
This module provides a coroutine to collect random
numbers using async comprehension.
"""

from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async
    comprehension over async_generator.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    return [number async for number in async_generator()]
