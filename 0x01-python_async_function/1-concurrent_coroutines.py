#!/usr/bin/env python3
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    x = []
    for delay in range(n):
        x.append(wait_random(max_delay))
    return [await a for a in asyncio.as_completed(x)]
