#!/usr/bin/env python3
""" test utils module """
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
)


class TestAccessNestedMap(unittest.TestCase):
    """ class TestAccessNestedMap """
    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any):
        """Test access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError),
        ]
    )
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence, expected: Any):
        """Test access nested map exception"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ class TestGetJson """
    @parameterized.expand(
        [
            ("https://example.com", {"payload": True}),
            ("https://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, url: str, expected: Any):
        """ Test the get_json function with different
        URLs and expected JSON responses """
        with patch("utils.requests.get") as mock_get:
            mock_get.return_value.json.return_value = expected
            self.assertEqual(get_json(url), expected)
