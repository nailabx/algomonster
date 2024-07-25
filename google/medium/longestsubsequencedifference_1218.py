from typing import Dict, List
from collections import defaultdict
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp: Dict = defaultdict(int)
        res: int = 0
        for num in arr:
            dp[num] = dp[num - difference] + 1
            res = max(res, dp[num])
                
        return res