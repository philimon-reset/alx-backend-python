#!/usr/bin/env python3
""" Second async task

    Returns:
        [list]: [list of delay times]
    """

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Main function of task

    Args:
        n (int): [Amount of calls to wait_random]
        max_delay (int): [delay specification]

    Returns:
        [list]: [list of delay time]
    """
    x = []
    for delay in range(n):
        x.append(wait_random(max_delay))
    return [await a for a in asyncio.as_completed(x)]
