#!/usr/bin/env python3
"""
  type annotation basics
"""

from typing import TypeVar, Mapping, Union, Any

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """usage of typevar and adding proper annotations"""
    if key in dct:
        return dct[key]
    else:
        return default
