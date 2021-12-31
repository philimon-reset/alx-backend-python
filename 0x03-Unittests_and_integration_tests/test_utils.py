#!/usr/bin/env python3
"""  write the first unit test for utils.access_nested_map
    """

import unittest
from typing import Mapping, Sequence
from utils import access_nested_map
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(unittest.TestCase):
    """ Test Access nested map function
    Args:
        unittest ([type]): Inherited unittest method
    """
    @parameterized.expand([
        [{"a": 1}, ("a",), 1],
        [{"a": {"b": 2}}, ("a",), {"b": 2}],
        [{"a": {"b": 2}}, ("a", "b"), 2]
    ])
    def test_access_nested_map(
            self,
            nested: Mapping,
            path: Sequence,
            expected: int) -> None:
        """ test function """
        self.assertEqual(access_nested_map(nested, path), expected)

    @parameterized.expand([
        [{}, ("a",)],
        [{"a": 1}, ("a", "b")]
    ])
    def test_access_nested_map_exception(self, nested, path):
        """ Testing errors raised
        """
        with self.assertRaises(KeyError) as expected_E:
            access_nested_map(nested, path)
        self.assertEqual(expected_E.exception.args[0], path[-1])
