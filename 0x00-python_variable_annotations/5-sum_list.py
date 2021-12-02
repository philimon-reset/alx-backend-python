#!/usr/bin/env python3
"""
  type annotation basics
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns the sum of floats"""
    return sum(input_list)
