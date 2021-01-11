#!/usr/bin/env python3
"""
Test Access Nested Map docstring for holberton checker
"""

import requests
from parameterized import parameterized
from unittest import mock
import unittest
from utils import access_nested_map, get_json
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test Access Nested Map docstring for holberton checker
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, mapp, path, expected):
        """
        Test Access Nested Map docstring for holberton checker

        """
        self.assertEqual(access_nested_map(mapp, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, mapp, path):
        """
        Test Access Nested Map docstring for holberton checker

        """
        with self.assertRaises(KeyError):
            access_nested_map(mapp, path)


class TestGetJson(unittest.TestCase):
    """
    Test Access Nested Map docstring for holberton checker
    """
    @parameterized.expand([("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})])
    def test_get_json(self, test_url, test_payload):
        """ Test Access Nested Map docstring for holberton checker """
        mock = unittest.mock.Mock()
        mock.json.return_value = test_payload
        with unittest.mock.patch('requests.get', return_value=mock):
            request = get_json(test_url)
            mock.json.assert_called_once()
            self.assertEqual(request, test_payload)


class TestMemoize(unittest.TestCase):
    """ Test Access Nested Map docstring for holberton checker """
    def test_memoize(self):
        """ Test Access Nested Map docstring for holberton checker """
        class TestClass:
            """ Test Access Nested Map docstring for holberton checker """
            def a_method(self):
                """ Test Access Nested Map docstring for holberton checker """
                return 42

            @memoize
            def a_property(self):
                """ Test Access Nested Map docstring for holberton checker """
                return self.a_method()

        with mock.patch.object(TestClass, 'a_method') as obj:
            """ Test Access Nested Map docstring for holberton checker """
            mem = TestClass()
            mem.a_property()
            mem.a_property()
            obj.assert_called_once()
