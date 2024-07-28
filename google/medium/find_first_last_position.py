from typing import List
class FirstAndLastposition:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l: int = 0
        r: int = len(nums)-1
        a: int = -1
        b: int = -1

        while l<=r:
            mid: int = (l+r)//2
            if nums[mid] == target:
                a = mid
                r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        l: int = 0
        r: int = len(nums)-1

        while l<=r:
            mid: int = (l+r)//2
            if nums[mid] == target:
                b = mid
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return [a, b]


