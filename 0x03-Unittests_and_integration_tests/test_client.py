#!/usr/bin/env python3
"""  write the second unittest for client
    """

import unittest
from unittest.mock import DEFAULT, MagicMock, PropertyMock, patch
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

    def test_public_repos_url(self):
        """ testing _public_repos_url method """
        with patch("test_client.GithubOrgClient.org",
                   new_callable=PropertyMock,
                   return_value={"repos_url": "google-ish"}) as m:
            access = GithubOrgClient("google-ish")
            test = access._public_repos_url
            m.assert_called_once()
            self.assertEqual(test, m.return_value["repos_url"])
