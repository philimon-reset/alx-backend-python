#!/usr/bin/env python3
"""  write the first unit test for utils.access_nested_map
    """

import unittest
from unittest.mock import MagicMock, patch
from typing import Mapping, Sequence
from utils import access_nested_map, get_json, memoize
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
        """ test function access nested map with valid values """
        self.assertEqual(access_nested_map(nested, path), expected)

    @parameterized.expand([
        [{}, ("a",)],
        [{"a": 1}, ("a", "b")]
    ])
    def test_access_nested_map_exception(self, nested, path):
        """ Testing errors raised on access nested map
        """
        with self.assertRaises(KeyError) as expected_E:
            access_nested_map(nested, path)
        self.assertEqual(expected_E.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """ Getjson testing class

    Args:
        unittest ([type]): Inherited unittest method
    """
    @parameterized.expand([
        ["http://example.com", {"payload": True}],
        ["http://holberton.io", {"payload": False}]
    ])
    def test_get_json(self, test_url, test_payload):
        """ Testing get json valid values """
        with patch("test_utils.get_json", return_value=test_payload) as m:
            main_result = get_json(test_url)
        self.assertEqual(main_result["payload"], test_payload["payload"])
