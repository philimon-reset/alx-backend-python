#!/usr/bin/env python3
""" Thrid async task

    Returns:
        [float]: [time for execution]
    """
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int):
    """ Main function of task
    mesuring the time of execution

    Args:
        n (int): [number of times wait_Random is called]
        max_delay (int): [individual delay time]

    Returns:
        [float]: [total execution time]
    """
    start = time.perf_counter()
    res = asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n
