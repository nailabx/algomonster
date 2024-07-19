from utils.node import Node
from typing import List, Deque
from collections import deque

class CloneAryTree:
    def cloneTree(self, root: Node) -> Node:
        if not root:
            return None
        
        parent: Node = Node(root.val)
        stack: Deque = deque([root])
        copy_stack: Deque = deque([parent])
        while stack:
            node: Node = stack.pop()
            copy_node: Node = copy_stack.pop()
            tmp: List[Node] = []
            for n in node.children:
                if n:
                    copy_n = Node(n.val)
                    stack.append(n)
                    copy_stack.append(copy_n)
                    tmp.append(copy_n)
            copy_node.children = tmp
        return parent
