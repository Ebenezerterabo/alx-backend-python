#!/usr/bin/env python3
""" 1-concurrent_coroutines """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returns the list of all the delays"""
    tasks = []
    for i in range(n):
        tasks.append(wait_random(max_delay))
    return [await task for task in asyncio.as_completed(tasks)]
