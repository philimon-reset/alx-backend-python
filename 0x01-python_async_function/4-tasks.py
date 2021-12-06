#!/usr/bin/env python3
""" Fourth async task

    Returns:
        [list]: [list of delay times]
    """
import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Main function of tasks
    Same as wait_n but uses _asyncio.Task

    Args:
        n (int): [Amount of calls to wait_random]
        max_delay (int): [delay specification]

    Returns:
        [list]: [list of delay time]
    """
    x = []
    for delay in range(n):
        x.append(task_wait_random(max_delay))
    return [await a for a in asyncio.as_completed(x)]
