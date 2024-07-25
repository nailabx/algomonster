from collections import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n: int = len(height)
        left: int = 0
        right: int = n-1
        
        water: int = 0
        while left <= right:
            water = max(water, (right - left) * min(height[left], height[right]))
            if height[left]<= height[right]:
                left += 1
            else:
                right -= 1
        return water