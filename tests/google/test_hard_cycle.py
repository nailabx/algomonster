import unittest
from google.hard.longest_cycle import LongestCycle

class TestLongestCycle(unittest.TestCase):

    def setUp(self) -> None:
        self.g = LongestCycle()

    # def test_longest_cycle(self):
    #     edges = [3,3,4,2,3]
    #     res = self.g.longestCycle(edges)
    #     print(res)
    
    def test_with_weird(self):
        edges = [2,-1,3,1]
        res = self.g.longestCycle(edges)
        print(res)

