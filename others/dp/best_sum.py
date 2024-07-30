from typing import List, Optional, Dict
class GetTheBestSum:
    def bestSUm(self, target: int, nums: List[int], memo: Dict = {})->Optional[List[int]]:
        if target in memo:
            return memo[target]
        if target == 0:
            return []
        
        if target < 0:
            return None
        shortestCombination: List[int] = []
        for num in nums:
            remainder: Optional[List[int]] = self.bestSUm(target - num, nums, memo)
            if remainder is not None:
                combination: List[int] = remainder + [num]
                if not len(shortestCombination) or len(combination) < len(shortestCombination):
                    shortestCombination = combination
        memo[target] = shortestCombination
        return memo[target]
    
    def bestSUmTab(self, target: int, nums: List[int], memo: Dict = {})->Optional[List[int]]:
        tab: List[int] = [None] *(target + 1)
        tab[0] = []
        for i in range(target + 1):
            if tab[i] is not None:
                for num in nums:
                    if num + i <= target:
                        comb: List[int] = tab[i] + [num]
                        if tab[i + num] is None or len(tab[i + num]) > len(comb):
                            tab[i + num] = comb
        print(tab)
        return tab[target]


if __name__ == "__main__":
    l: GetTheBestSum = GetTheBestSum()
    target: int = 7
    nums: List[int] = [5, 3, 4, 7]
    print(l.bestSUmTab(target, nums))