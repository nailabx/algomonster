from typing import Dict
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count: Dict = defaultdict(int)
        l: int = 0
        n: int = len(s)
        res: int = 0
        for r in range(n):
            count[s[r]] += 1
            while l<r and count[s[r]]>1:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
                
        