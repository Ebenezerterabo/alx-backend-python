#!/usr/bin/env python3
"""" 4-tasks.py """

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """returns the list of all the delays"""
    tasks = []
    for i in range(n):
        tasks.append(task_wait_random(max_delay))
    return [await task for task in asyncio.as_completed(tasks)]
