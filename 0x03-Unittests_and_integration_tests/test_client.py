#!/usr/bin/env python3
"""Generic test utilities for github org client.
"""
import unittest
from unittest.mock import patch, MagicMock, Mock
from parameterized import parameterized  # type: ignore
from client import GithubOrgClient
from typing import (
    Any,
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

    def test_public_repos(self, url: str, expected: Any, mock_get_json: Mock):
        """ Implement the test_public_repos method to unit test
            the public_repos method of the GithubOrgClient class.
        """
        mock_get_json.return_value = MagicMock(return_value=expected)
        client = GithubOrgClient("org")
        self.assertEqual(client.public_repos(), expected)
        mock_get_json.assert_called_once_with(url)

    @patch("client.GithubOrgClient.public_repos")
    def test_public_repos(self, url: str, expected: Any, mock_get_json: Mock):
        """ Implement the test_public_repos method to unit test
            the public_repos method of the GithubOrgClient class.
        """
        mock_get_json.return_value = MagicMock(return_value=expected)
        client = GithubOrgClient("org")
        self.assertEqual(client.public_repos(), expected)
        mock_get_json.assert_called_once_with(url)

    def test_has_license(self, url: str, expected: Any, mock_get_json: Mock):
        """ Implement the test_has_license method to unit test
            the has_license method of the GithubOrgClient class.
        """
        mock_get_json.return_value = MagicMock(return_value=expected)
        client = GithubOrgClient("org")
        self.assertEqual(client.has_license(repo=expected), expected)
        mock_get_json.assert_called_once_with(url)
