from typing import Dict
class Solution:
    def fibonnaciMemo(self, n: int, memo: Dict[int, int] = {})->int:
        if n in memo:
            return memo[n]
        
        if n < 2:
            return 1
        
        memo[n] = self.fibonnaciMemo(n - 2, memo) + self.fibonnaciMemo(n - 1, memo)
        return memo[n]
