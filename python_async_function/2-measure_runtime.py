#!/usr/bin/env python3
"""
This module provides a function to measure the runtime of wait_n.
"""

import time
import asyncio
from typing import Callable
from concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay) and
    return the average time per task.

    Args:
        n (int): The number of tasks to run.
        max_delay (int): The maximum delay for each task.

    Returns:
        float: The average execution time per task.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    total_time = end_time - start_time
    return total_time / n
