from collections import deque
from typing import Deque, List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n: int = len(nums)
        res: List[int] = []
        queue: Deque = deque([])
        for i in range(k):
            while queue and queue[-1][0] <= nums[i]:
                queue.pop()
            queue.append((nums[i], i))
        res.append(queue[0][0])

        for i in range(k, n):
            if i - k == queue[0][1]:
                queue.popleft()
            while queue and queue[-1][0] <= nums[i]:
                queue.pop()
            queue.append((nums[i], i))
            res.append(queue[0][0])   
        return res        

        