#!/usr/bin/env python3
""" Async python first tasks
    takes an int representing the time of delay and return it

    Returns:
        int: delay appointed by max_delay
    """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Main function of the task

    Args:
        max_delay (int): [description]. Defaults to 10.

    Returns:
        int: [delay time]
    """
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
