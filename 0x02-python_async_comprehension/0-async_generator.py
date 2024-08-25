#!/usr/bin/env python3
""" 0-async_generator.py """
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """" loop 10 times each time asynchronously wait 1 second """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
