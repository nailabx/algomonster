from typing import List, Dict
from collections import defaultdict

class LongestCycle:
    """
    We are going to use DFS, For each edges we add it into our path 
    and add it into visited.
    Then for each neighbor we check if it already exist if so then it is cycle
    add the cycle into the list of answer.
    At the end return the longest path.
    Since we are going through each edge and vertices 
    Time complexity is O(v + E)
    Space complexity O(E)
    """
    def longestCycle(self, edges: List[int]) -> int:
        def build(edges: List[int]) -> Dict[int, List[int]]:
            res = defaultdict(list)
            for i, v in enumerate(edges):
                if v<0:
                    res[i] += []
                else:
                    res[i].append(v)
            return res
        
        graph: Dict[int, List[int]] = build(edges)

        cycles = []

        def dfs(node, visited, current_path):
            visited[node] = True
            current_path.append(node)

            for neighbor in graph[node]:
                if neighbor in current_path:
                    start_index = current_path.index(neighbor)
                    cycle = current_path[start_index:]
                    cycles.append(cycle)
                elif not visited[neighbor]:
                    dfs(neighbor, visited, current_path)

            current_path.pop()
            visited[node] = False

        visited = {node: False for node in graph}
        for node in graph:
            if not visited[node]:
                dfs(node, visited, [])

        return len(max(cycles, key=len)) if cycles else 0
