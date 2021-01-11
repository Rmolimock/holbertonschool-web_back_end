#!/usr/bin/env python3
''' test_client module doctstring for holberton checker '''

from parameterized import parameterized
from unittest import TestCase, mock
import client
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    ''' Test Github Org class doc string '''

    @parameterized.expand([
        ('buttercup'),
        ('verne'),
        ('koi')])
    @mock.patch('client.get_json')
    def test_gorg(self, gorg, m):
        ''' Test Github Org class doc string '''
        client.GithubOrgClient(gorg).org()
        m.assert_called_once_with(f'https://api.github.com/orgs/{gorg}')

    def test_public_repos_url(self):
        ''' Test Github Org class doc string '''
        with mock.patch('client.GithubOrgClient._public_repos_url',
                        new_callable=mock.PropertyMock) as mk:
            mk.return_value = 'test'
            g_client = GithubOrgClient('something')
            pub_rurl = g_client._public_repos_url
            self.assertEqual(pub_rurl, 'test')
