from typing import List, Set, Tuple, Deque
from collections import deque

class NumIslands:
    def numIslands(self, grid: List[List[str]]) -> int:
        n: int = len(grid)
        m: int = len(grid[0])
        count: int = 0
        visited: Set =  set()

        def dfs(x: int, y: int)->int:
            if x < 0 or x>= n or y < 0 or y >= m or grid[x][y] == "0" or (x, y) in visited :
                return 
            visited.add((x, y))
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count
    
    def numIslands_queue(self, grid: List[List[str]])-> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        def get_neighbors(coord):
            row, col = coord
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0, -1]
            for i in range(len(delta_row)):
                r = row + delta_row[i]
                c = col + delta_col[i]
                if 0 <= r < num_rows and 0 <= c < num_cols:
                    yield r, c
        
        def bfs(start: Tuple[int, int]):
            queue = deque([start])
            r, c = start
            grid[r][c] = "0"
            while len(queue) > 0:
                node = queue.popleft()
                for neighbor in get_neighbors(node):
                    r, c = neighbor
                    if grid[r][c] == "0":
                        continue
                    queue.append(neighbor)
                    grid[r][c] = "0"
        
        count = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "0":
                    continue
                bfs((r, c))
                count += 1 
        return count



