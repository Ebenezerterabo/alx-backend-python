#!/usr/bin/env python3
""" test utils module """
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Dict,
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
        mock_response = Mock()
        mock_response.json.return_value = expected
        with patch("utils.requests.get") as mock_get:
            mock_get.return_value = mock_response
            self.assertEqual(get_json(url), expected)


class TestMemoize(unittest.TestCase):
    """ class TestMemoize """
    def test_memoize(self):
        """ Test the memoize decorator """
        class TestClass:
            """ TestClass """
            def a_method(self):
                """ a_method """
                return 42

            @memoize
            def a_property(self):
                """ a_property """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock.assert_called_once()
