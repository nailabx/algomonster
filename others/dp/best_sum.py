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


if __name__ == "__main__":
    l: GetTheBestSum = GetTheBestSum()
    target: int = 7
    nums: List[int] = [2, 3, 4]
    print(l.bestSUm(target, nums))