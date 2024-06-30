from collections import deque
from typing import List, Callable
class Node:
    def __init__(self, val: any, left=None, right=None) -> None:
        self.val: any = val
        self.left: Node = left
        self.right: Node = right

    def __str__(self):
        res = []
        q: List[Node] = deque([self])
        while q:
            n = q.popleft()
            if n:
                res.append(n.val)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        return f"{res}"
