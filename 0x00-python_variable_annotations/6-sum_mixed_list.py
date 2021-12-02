#!/usr/bin/env python3
"""
  type annotation basics
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum of mxd list"""
    return sum(mxd_lst)
