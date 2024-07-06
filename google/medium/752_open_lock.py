from typing import List, Deque, Dict, Set
from collections import deque
class OpenLock:

    def openLock(self, deadends: List[str], target: str) -> int:
        next_digits = {**{str(i): str(i + 1) for i in range(9)}, "9": "0"}
        prev_digits = {v:k for k, v in next_digits.items()}
        
        def bfs():
            blocked: Set[str] = set(deadends)
            steps: Dict[str, int] = {
                "0000": 0
            }
            if target == "0000":
                return 0
            
            if "0000" in blocked:
                return -1
            queue: Deque = deque({"0000"})
            while queue:
                top = queue.popleft()
                for i in range(4):
                    new_top = top[0:i] + next_digits[top[i]] + top[i+1:]
                    if new_top not in blocked and new_top not in steps:
                        queue.append(new_top)
                        steps[new_top] = steps[top] + 1
                        if new_top == target:
                            return steps[top] 
                    
                    new_top = top[0:i] + prev_digits[top[i]] + top[i+1:]
                    if new_top not in blocked and new_top not in steps:
                        queue.append(new_top)
                        steps[new_top] = steps[top] + 1
                        if new_top == target:
                            return steps[top] 
            return -1
        return bfs()