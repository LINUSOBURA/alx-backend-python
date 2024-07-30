#!/usr/bin/env python3
"""
Test Utils
"""

import unittest

from parameterized import parameterized

from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test Access Nested Map"""

    @parameterized.expand([({
        "a": 1
    }, ["a"], 1), ({
        "a": {
            "b": 2
        }
    }, ["a"], {
        "b": 2
    }), ({
        "a": {
            "b": 2
        }
    }, ["a", "b"], 2)])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ["a"], 'a'), ({"a", 1}, ["a", "b"], 'a')])
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        """Test access nested map exception"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception.args[0]), expected_key)
