from collections import defaultdict
from typing import Dict, List, Optional
from utils.tree_node import TreeNode

class BinaryTreeFromDesc:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        n: int = len(descriptions)
        if n == 0:
            return None
        root: int = -1
        parent: Dict = {}
        node: Dict = {}

        for parentVal, nodeVal, pos in descriptions:
            if parentVal not in node:
                node[parentVal] = TreeNode(parentVal)
                if parentVal not in parent:
                    root = parentVal
            if nodeVal not in node:
                node[nodeVal] = TreeNode(nodeVal)
            parent[nodeVal] = parentVal

            if pos:
                node[parentVal].left = node[nodeVal]
            else:
                node[parentVal].right = node[nodeVal]
        # print(parent)
        while root in parent:
            root = parent[root]
        return node[root]