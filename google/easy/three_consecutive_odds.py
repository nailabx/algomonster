from typing import List

class ThreeConsecutiveOdds:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        l, r = 0, 0
        n: int = len(arr)
        for i in range(n):
            if arr[i]%2 != 0:
                r += 1
            if arr[i] % 2 == 0:
                l = r
            if r - l > 2:
                return True
        return False