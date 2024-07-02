import unittest
from google.easy.array_intersection_2 import ArrayIntersection
from typing import List

class TestArrayIntersection2(unittest.TestCase):

    def setUp(self) -> None:
        self.a = ArrayIntersection()

    def test_two_distinct_array(self):
        nums1: List[int] = [4,9,5]
        nums2: List[int] = [9,4,9,8,4]
        expected: List[int] = [4,9]
        res = self.a.intersect(nums1, nums2)
        self.assertListEqual(res, expected)
    
    def test_using_map(self):
        nums1: List[int] = [4,9,5]
        nums2: List[int] = [9,4,9,8,4]
        expected: List[int] = [4,9]
        res = self.a.intersect_with_map(nums1, nums2)
        self.assertListEqual(sorted(res), expected)
    
    def test_intersection_using_builtin(self):
        nums1: List[int] = [4,9,5]
        nums2: List[int] = [9,4,9,8,4]
        expected: List[int] = [4,9]
        res = self.a.intersection_using_builtin(nums1, nums2)
        self.assertListEqual(sorted(res), expected)
