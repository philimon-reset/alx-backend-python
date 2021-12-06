#!/usr/bin/env python3
import asyncio
import random

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int):
    x = []
    for delay in range(n):
        x.append(task_wait_random(max_delay))
    return [await a for a in asyncio.as_completed(x)]
