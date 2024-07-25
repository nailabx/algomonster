from typing import List
class MergeSort:
    def merge(self, left_arr: List[int], right_arr: List[int], left_size: int, right_size: int, res: List[int])->None:
        l, r, i = 0, 0, 0
        while l<left_size and r<right_size:
            if left_arr[l] < right_arr[r]:
                res[i] = left_arr[l]
                i += 1
                l += 1
            else:
                res[i] = right_arr[r]
                i += 1
                r += 1
        
        while l< left_size:
            res[i] = left_arr[l]
            i += 1
            l += 1
        while r < right_size:
            res[i] = right_arr[r]
            i += 1
            r += 1
    
    def mergeSort(self, nums: List[int])->None:
        n: int = len(nums)
        if n<2:
            return
        mid: int = n//2
        left_arr: List[int] = nums[:mid]
        right_arr: List[int] = nums[mid:]
        self.mergeSort(left_arr)
        self.mergeSort(right_arr)

        self.merge(left_arr, right_arr, mid, n - mid, nums)
    

