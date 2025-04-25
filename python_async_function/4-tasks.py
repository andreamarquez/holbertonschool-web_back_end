#!/usr/bin/env python3
"""
This module provides a function to run multiple tasks
concurrently using task_wait_random.
"""

import asyncio
from typing import List
from tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay and return
    the list of all delays in ascending order.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay for task_wait_random.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    completed_delays = []
    for task in asyncio.as_completed(tasks):
        completed_delays.append(await task)

    return completed_delays
