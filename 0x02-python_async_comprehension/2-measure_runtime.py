#!/usr/bin/env python3
""" Third task from async2 project
    """
import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure the runtime of async_comp

    Returns:
        float: [Runtime]
    """
    start = time.time()
    res = await asyncio.gather(*(async_comprehension() for x in range(4)))
    end = time.time() - start
    return end
