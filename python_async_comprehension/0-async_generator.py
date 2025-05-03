#!/usr/bin/env python3
"""
This module provides an asynchronous generator that yields random numbers.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields 10 random numbers between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
