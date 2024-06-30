import unittest
from dsa.models.node import Node
from dsa.dfs.dfs_tree import build_tree
class TestNode(unittest.TestCase):

    def test_create_node(self):
        l = [1, 2, 3, 4, 5, 6, 7]
        n = build_tree(iter(l), int)
        tree = eval(f"{n}")
        self.assertEqual(n.val, 1)

if __name__ == '__main__':
    unittest.main()