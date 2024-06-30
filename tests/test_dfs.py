from dsa.models.node import Node
from dsa.dfs.dfs_tree import build_tree
from dsa.dfs.dfs_tree import DfsTree
import unittest

class test_dfs(unittest.TestCase):

    def setUp(self) -> None:
        self.dfs = DfsTree()
    
    def test_pre_order_traversal(self):
        l = iter(["A", "B", "G", "C", "D", "x",  "H", "x", "x", "E", "F"])
        root = build_tree(l, str)
        res1 = self.dfs.pre_order_traversal_recursive(root=root)
        res2 = self.dfs.pre_order_traversal_stack(root=root)
        self.assertListEqual(res1, res2)

    
    def test_in_order_traversal(self):
        l = iter(["A", "B", "G", "C", "D", "x",  "H", "x", "x", "E", "F"])
        root = build_tree(l, str)
        res1 = self.dfs.in_order_traversal_recursive(root=root)
        res2 = self.dfs.in_order_traversal_stack(root=root)
        self.assertListEqual(res1, res2)

    def test_post_order_traversal(self):
        l = iter(["F", "B", "G", "A", "D", "x", "H", "x", "x", "C", "E"])
        root = build_tree(l, str)
        res = self.dfs.post_order_traversal_recursive(root)
        self.assertIsNotNone(res)

    def test_find_target(self):
        data = iter([1,2, 3, "x", 5, "x", "x", 4, "x", "x", 6])
        root = build_tree(data, int)
        target: int = 3
        res1 = self.dfs.find_target_rec(root, target)
        res2 = self.dfs.find_target_st(root, target)
        self.assertEqual(res1, res2)

    def test_print(self):
        data = iter(["/", "Foo", "Baz", "x", "x", "x", "Bar"])
        root = build_tree(data, str)
        res = self.dfs.pretty_print(root)
        self.assertIsNotNone(res)

    def test_min_max(self):
        data = iter([5, 1, 8, "x", "x", 11, "x", "x"])
        root = build_tree(data)
        min_val = self.dfs.min_element(root)
        max_val = self.dfs.max_element(root)
        self.assertEqual(min_val, 1)
        self.assertEqual(max_val, 11)
    def test_depth(self):
        data = iter([5, 4, 3, "x", "x", 8, "x", "x", 6, "x", "x"])
        root = build_tree(data)
        res = self.dfs.tree_max_depth(root)
        self.assertEqual(res, 2)
    
    def test_serialize(self):
        data = [5, 4, 3, "x", "x", 8, "x", "x", 6, "x", "x"]
        root: Node = build_tree(iter(data))
        encoded = self.dfs.serialize(root)
        decoded = self.dfs.deserialize(encoded)
        self.assertEqual(len(data), len(encoded.split(",")))
        self.assertEqual(root.val, decoded.val)


    def test_invert_binary_tree(self):
        data = [5, 4, 3, "x", "x", 8, "x", "x", 6, "x", "x"]
        root: Node = build_tree(iter(data))
        res = self.dfs.invert_binary_tree(root=root)
        # print(self.dfs.serialize(res))

    def test_bst(self):
        data = [6, 4, 3, "x", "x", 5, "x", "x", 8, "x", "x"]
        root: Node = build_tree(iter(data))
        res = self.dfs.valid_bst(root=root)
        self.assertTrue(res)
    
    def test_insert_bst(self):
        data = [6, 4, 3, "x", "x", 5, "x", "x", 8, "x", "x"]
        root: Node = build_tree(iter(data))
        res = self.dfs.insert_bst(root, 7)
        # print(self.dfs.serialize(res))





if __name__ == "__main__":
    unittest.main()