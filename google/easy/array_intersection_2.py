from typing import List, Dict
from collections import Counter
class ArrayIntersection:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        n,m = len(nums1), len(nums2)
        ans: List[int] = []
        while i<n and j<m:
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i]<nums2[j]:
                i += 1
            else:
                j += 1
        return ans
    
    def intersect_with_map(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_nums1: Dict[int, int] = Counter(nums1)
        ans: List[int] = []
        for num in nums2:
            if num in count_nums1 and count_nums1[num] > 0:
                ans.append(num)
                count_nums1[num] -= 1
        return ans
    
    def intersection_using_builtin(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return (Counter(nums1)&Counter(nums2)).elements()
            
