#!/usr/bin/env python3
"""Generic test utilities for github org client.
"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient
from typing import (
    Any,
    Mock
)


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient class"""

    @parameterized.expand([
        ("google", {'login': 'google'}),
        ("abc", {'login': 'abc'}),
    ])
    def test_org(self, org_name: str, expected: Any, mock_get_json: Mock):
        """Test org"""
        mock_get_json.return_value = MagicMock(return_value=expected)
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org(), expected)
        mock_get_json.assert_called_once_with(
            client.ORG_URL.format(org=org_name))
