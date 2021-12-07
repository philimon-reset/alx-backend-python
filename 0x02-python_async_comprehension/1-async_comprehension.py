#!/usr/bin/env python3
""" Async python second task
    async_comprehension return the 10 random numbers.
    """

import asyncio
import random
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """ save the random number yielded from a function
    """
    x = [i async for i in async_generator()]
    return x
