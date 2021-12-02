#!/usr/bin/env python3
from typing import Union, Tuple

"""
  type annotation basics
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple(str, float):
    """returns a tuple with k and square of v"""
    return (k, float(v**2))
