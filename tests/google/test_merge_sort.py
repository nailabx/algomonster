from unittest import TestCase
from typing import List
from google.medium.merge_sort import MergeSort
class TestMergeSort(TestCase):

    def test_mergesort(self):
        nums: List[int] = [12,1,10,50,5,15,45]
        m: MergeSort = MergeSort()
        m.mergeSort(nums)
        print(nums)