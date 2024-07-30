from typing import List, Optional, Dict
class ListOfSum:
    def howAllSum(self, target:int, numbers: List[int])->Optional[List[List[int]]]:
        ans: List[List[int]] = []
        def dfs(target: int, nums: List[int], curr: List[List[int]], start: int= 0)->None:
            if target == 0:
                ans.append(curr[:])
                return
            if target < 0:
                return
            for i in range(start, len(nums)):
                remainder: int = target - nums[i]
                dfs(remainder, nums, curr + [nums[i]])
        dfs(target, numbers, [], 0)
        return ans
    
    def howSum(self, target: int, nums: List[int], memo: Dict[int, List[int]]= {})->Optional[List[int]]:
        if target in memo:
            return memo[target]
        if target == 0:
            return []
        if target < 0:
            return None
        
        for num in nums:
            res: Optional[List[int]] = self.howSum(target - num, nums)
            if res is not None:
                memo[target - num] =  res + [num]
                return memo[target - num]
        return None

    def howSumTab(self, target: int, nums: List[int], memo: Dict[int, List[int]]= {})->Optional[List[int]]:
        tab: List[int] = [None] * (target + 1)
        tab[0] = []
        print(tab)
        for i in range(target + 1):
            if tab[i] is not None:
                for num in nums:
                    if i + num <= target:
                        tab[i + num] = tab[i] + [num]
        return tab[target]




if __name__ == "__main__":
    l: ListOfSum = ListOfSum()
    target: int = 7
    nums: List[int] = [5, 3, 4, 7]
    print(l.howSumTab(target, nums))