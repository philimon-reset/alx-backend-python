#!/usr/bin/env python3
""" Fourth async task

    Returns:
        [_asyncio.Task]: [return an async task object]
    """
import asyncio
import random
from typing import Coroutine

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Coroutine:
    """ Returns: _asyncio.Task: _asyncio.Task object"""
    return asyncio.create_task(wait_random(max_delay))
