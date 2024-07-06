from collections import deque
from typing import Deque, List, Tuple

class WallsAndGates:
    def wallsAndGates(self, rooms: List[List[int]])->None:
        queue: Deque = deque()
        n: int = len(rooms)
        m: int = len(rooms[0])
        INF: int = 2147483647

        DIRECTIONS: List[Tuple[int, int]] = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        for row in range(n):
            for col in range(m):
                if rooms[row][col] == 0:
                    queue.append((row, col))

        while queue:
            row, col = queue.popleft()
            for x, y in DIRECTIONS:
                cur_x = row + x
                cur_y = col + y
                if 0<= cur_x <n and 0<= cur_y <m:
                    if rooms[cur_x][cur_y] == INF:
                        rooms[cur_x][cur_y] = rooms[row][col] + 1
                        queue.append((cur_x, cur_y))