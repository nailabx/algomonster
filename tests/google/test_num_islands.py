import unittest
from typing import List
from google.medium.num_islands import NumIslands

class TestNumIsland(unittest.TestCase):

    def setUp(self) -> None:
        self.g = NumIslands()

    def test_num_islands(self):
        grid: List[List[int]] = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        res = self.g.numIslands(grid=grid)
        self.assertEqual(res, 1)
    def test_num_islands_2(self):
        grid: List[List[int]] = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        res = self.g.numIslands(grid=grid)
        self.assertEqual(res, 3)
    
    def test_num_islands_queue(self):
        grid: List[List[int]] = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        res = self.g.numIslands_queue(grid=grid)
        self.assertEqual(res, 3)

