#!/usr/bin/env python3
from typing import Callable

"""
  type annotation basics
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function"""
    def func(num: float) -> float:
        return multiplier * num
    return func
