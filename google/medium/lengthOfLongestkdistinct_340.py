from collections import defaultdict
from typing import Dict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n: int = len(s)
        if k<= 0:
            return 0
        if(n <= k):
            return n
        count: Dict[int] = defaultdict(int)
        l: int = 0
        res: int = 0
    
        for r in range(n):
            count[s[r]] += 1            
            # print(f"l={l} and r={r}")
            while l< r and len(count)>k:
                # print(f"I am here")
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
            res = max(res, r - l + 1) 
        return res
        