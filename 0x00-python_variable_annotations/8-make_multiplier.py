#!/usr/bin/env python3
"""
  type annotation basics
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function"""
    def func(num: float) -> float:
        return multiplier * num
    return func
