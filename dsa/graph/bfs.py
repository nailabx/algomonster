from typing import Dict, List, Deque
from collections import deque

class BFS:
    def shortest_path(self, graph: List[List[int]], a: int, b: int)->int:
        def get_neighbors(node: int):
            return graph[node]

        # BFS template
        def bfs(root: int, target: int):
            queue = deque([root])
            visited = set([root])
            level = 0
            while len(queue) > 0:
                n = len(queue)
                for n in range(n):
                    node = queue.popleft()
                    if node == target:
                        return level
                    for neighbor in get_neighbors(node):
                        if neighbor in visited:
                            continue
                        queue.append(neighbor)
                        visited.add(neighbor)
                level += 1

        return bfs(a, b)

