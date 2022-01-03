#!/usr/bin/env python3
"""  write the second unittest for client
    """

import unittest
from unittest.mock import MagicMock, patch
from typing import Mapping, Sequence
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """ class for githuborgclient class and whole client file """
    @parameterized.expand([["google"], ["abc"]])
    @patch.object(GithubOrgClient, "org")
    def test_org(self, org_T, mock):
        """ function to test GithuborgClient"""
        GithubOrgClient.org(org_T)
        mock.assert_called_once()
