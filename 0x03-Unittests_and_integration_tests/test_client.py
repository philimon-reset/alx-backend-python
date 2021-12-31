#!/usr/bin/env python3
""" Async python first task
    async_generator that takes no arguments
    """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Generate a random number after await

    Yields:
        [int]: [yield a value not stored in memory]
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 9)
