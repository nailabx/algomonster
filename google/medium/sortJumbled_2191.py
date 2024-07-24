from collections import deque
from collections import List, Tuple
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        to_be_sorted: List[Tuple] = []
        for idx, num in enumerate(nums):
            mapped_value: int = 0   
            temp = nums[idx]
            pos: int = 1   
            if temp == 0:
                to_be_sorted.append((idx, mapping[0]))
                continue
            
            while temp != 0:
                mapped_value = pos * mapping[temp%10] + mapped_value
                pos *= 10
                temp //= 10
            to_be_sorted.append((idx, mapped_value))
        to_be_sorted.sort(key=lambda x: x[1])
        res = [nums[idx] for idx, _ in to_be_sorted]
        return res
        