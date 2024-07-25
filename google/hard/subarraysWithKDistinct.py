from collections import List, defaultdict
from typing import Dict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums: List[int], k: int):
            n: int = len(nums)
            count: Dict = defaultdict(int)
            l: int = 0
            total: int = 0
            for r in range(n):
                count[nums[r]] += 1
                while len(count) > k:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        del count[nums[l]]
                    l += 1
                total += (r - l )
            return total
        return atMostK(nums, k) - atMostK(nums, k-1)
            

        