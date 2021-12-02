#!/usr/bin/env python3
from typing import List, Union

"""
  type annotation basics
"""


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """returns the sum of mxd list"""
    return sum(mxd_lst)
