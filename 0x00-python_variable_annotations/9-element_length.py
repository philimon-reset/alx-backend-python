#!/usr/bin/env python3
from typing import Iterable, Sequence, Tuple


"""
  type annotation basics
"""


def element_length(lst: Iterable[Sequence]) -> Iterable[Tuple[Sequence, int]]:
    """takes a list and returns a list of tuples"""
    return [(i, len(i)) for i in lst]
