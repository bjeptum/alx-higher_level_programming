#!/usr/bin/python3
"""Unitests for max_interger function."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_normal_list(self):
        """Test with a normal list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
    
    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
    
    def test_mixed_numbers(self):
        """Test with a mix of positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)
    
    def test_single_element(self):
        """Test with a single element"""
        self.assertEqual(max_integer([42]), 42)
    
    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))
    
    def test_identical_elements(self):
        """Test with identical elements"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)
    
    def test_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(max_integer([1000000000, 999999999]), 1000000000)
    
    def test_large_list(self):
        """Test with a very large list"""
        self.assertEqual(max_integer(list(range(1000000))), 999999)

if __name__ == '__main__':
    unittest.main()
