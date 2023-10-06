#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_none_list(self):
        "test for none list"
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_single_element_list(self):
        """Test a list with a single element."""
        a = [9]
        self.assertEqual(max_integer(a), 9)

    def test_normal_list(self):
        """Test an normal list of integers."""
        a = [10, 1, 9, 3]
        self.assertEqual(max_integer(a), 10)

    def test_floats(self):
        """Test a list of floats."""
        nums = [16.5, 2.54, 9.123, 15.25, 6.0]
        self.assertEqual(max_integer(nums), 16.5)

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_string(self):
        """Test a string."""
        self.assertEqual(max_integer("Gelfeto"), 't')
    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["baba", "dada", "mama", "kaka"]
        self.assertEqual(max_integer(strings), "mama")
if __name__ == '__main__':
    unittest.main()
