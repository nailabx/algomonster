from typing import List, Dict
class CanSumToTarget:
    def canSum(self, target: int, numbers: List[int])->bool:
        dp = [False] * (target + 1)
        dp[0] = True
        for i in range(target + 1):
            if dp[i]:
                for num in numbers:
                    if i + num <= target:
                        dp[i + num] = True
        print(dp)
        return dp[target]
    
    def canSumRecursive(self, target: int, numbers: List[int], memo: Dict[int, bool] = {})->bool:
        if target == 0:
            return True
        if target < 0:
            return False
        
        if target in memo:
            return memo[target]
        
        for num in numbers:
            remainder: int = target - num
            memo[remainder] = self.canSumRecursive(target- num, numbers, memo)
            if memo[remainder]:
                return True
        return False
    
if __name__ == "__main__":
    c = CanSumToTarget()
    target: int = 7
    numbers: List[int] = [2, 3]
    print(c.canSum(target, numbers))