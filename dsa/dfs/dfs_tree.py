from dsa.models.node import Node
from typing import List, Callable, Iterable
from collections import deque
from math import inf

class DfsTree:

    '''
    This two methods will return the in-order traversal.
    One is recursive and the other one is using stack 
    '''

    def in_order_traversal_recursive(self, root: Node)->list:
        res = []
        def in_order(root: Node) -> None:
            if root:
                in_order(root.left)
                res.append(root.val)
                in_order(root.right)
        in_order(root)
        return res
    
    def in_order_traversal_stack(self, root: Node) -> list:
        stack = deque([])
        res: list = []
        current = root
        while True:
            if current:
                stack.append(current)
                current = current.left 
            elif stack:
                current = stack.pop()
                res.append(current.val)
                current = current.right
            else:
                break
        return res



    '''
        This two methods will return the pre-order traversal.
        One is recursive and the other one is using stack 
    '''
    def pre_order_traversal_recursive(self, root: Node) -> list:
        res = []
        def pre_order(root: Node):
            if root:
                res.append(root.val)
                pre_order(root.left)
                pre_order(root.right)
        pre_order(root=root)
        return res
        


    def pre_order_traversal_stack(self, root: Node)->list:
        stack = deque([root])
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
        return res
    
    '''
    This two methods will return the post-order traversal.
    One is recursive and the other one is using stack 
    '''
    def post_order_traversal_recursive(self, root: Node)->list:
        res = []
        def post_order(root: Node)->None:
            if root:
                post_order(root.left)
                post_order(root.right)
                res.append(root.val)
        post_order(root=root)
        return res
    
    '''
    Find element in a binary tree: element is target
    '''
    def find_target_rec(self, root: Node, target):
        if not root:
            return None
        if root.val == target:
            return root
        return self.find_target_rec(root.left, target) or self.find_target_rec(root.right, target)
    
    def find_target_st(self, root:Node, target):
        if not root:
            return None
        stack = deque([root])
        while stack:
            node = stack.pop()
            if node.val == target:
                return node
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return None
    
    def pretty_print(self, root: Node)->list:
        res = []
        def print(root: Node, indent: str)->None:
            if not root:
                return 
            res.append(indent + root.val)
            indent += " "
            print(root.left, indent)
            print(root.right, indent)
        print(root, "")
        return res
    
    def max_element(self, root:Node)->int:
        if not root:
            return float("-inf")
        return max(root.val, self.max_element(root.left), self.max_element(root.right))
    
    def min_element(self, root:Node)->int:
        global min_val
        min_val = float("inf")
        def dfs(root:Node):
            global min_val
            if not root:
                return
            # print(f"comparing {min_val} and {root.val}")
            min_val = min(min_val, root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return min_val
    def tree_max_depth(self, root: Node) -> int:
        if not root:
            return 0
        def dfs(root:Node, dep):
            if not root:
                return dep
            return max(dfs(root.left, dep + 1), dfs(root.right, dep + 1))
        return dfs(root, -1)
    
    """
    In a binary tree, a node is labeled as "visible" if, on the path from the root to that node, there isn't any node with a value higher than this node's value.
    The root is always "visible" since there are no other nodes between the root and itself. Given a binary tree, count the number of "visible" nodes.
    """
    def visible_tree_node(self, root: Node) -> int:
        # WRITE YOUR BRILLIANT CODE HERE
        return 0

    '''
    Serialize and deserialize a tree
    '''
    def serialize(self, root: Node):
        res = []
        def dfs(root: Node):
            if not root:
                res.append("x")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ','.join(res)

    def deserialize(self, s:str):
        data = iter(s.split(","))
        def dfs(d: Iterable[str])->Node:
            try:
                val = next(d)
            except:
                val = "x"
            if val == "x":
                return None
            left = dfs(d)
            right = dfs(d)
            return Node(int(val), left, right)

        return dfs(data) 
        
    '''
    Given a binary tree, invert it and return the new value. You may invert it in-place.
    To "invert" a binary tree, switch the left subtree and the right subtree, and invert them both. Inverting an empty tree does nothing.
    '''
    def invert_binary_tree(self, root: Node) -> Node:
        if not root:
            return None
        self.invert_binary_tree(root.left)
        self.invert_binary_tree(root.right)
        root.left, root.right = root.right, root.left
        return root
    
    """
    A binary search tree is a binary tree with the property that for any node, the value of this node is greater than any node in its left subtree and less than any node's value in its right subtree. 
    In other words, an inorder traversal of a binary search tree yields a list of values that is monotonically increasing (strictly increasing).
    """
    def valid_bst(self, root: Node) -> bool:
        def dfs(root: Node, min_val: int, max_val: int)->bool:
            if not root:
                return True
            if not (min_val < root.val < max_val):
                return False
            return dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val)
        return dfs(root, -inf, inf)
    
    """
    Given the root node of a valid BST and a value to insert into the tree, return a new root node representing the valid BST with the addition of the new item. 
    If the new item already exists in the binary search tree, do not insert anything.
    You must expand on the original BST by adding a leaf node. Do not change the structure of the original BST.
    """
    def insert_bst(self, bst: Node, val: int) -> Node:
        def dfs(root: Node, val: int)->Node:
            if not root:
                return Node(val=val)
            if root.val < val:
                root.right = dfs(root.right, val)
            if root.val > val:
                root.left = dfs(root.left, val)
            return root
        return dfs(bst, val)




def build_tree(nodes: list, f: Callable = None) -> Node:
    left, right = None, None
    try:
        val = next(nodes)
    except StopIteration:
        val = "x"
    if val == "x": return None
    if f is None: f=int
    left = build_tree(nodes=nodes, f=f)
    right = build_tree(nodes=nodes, f=f)
    return Node(val=f(val), left=left, right=right) 