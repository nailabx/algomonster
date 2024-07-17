from typing import Dict
class RomanToInteger:
    def romanToInt(self, s: str) -> int:
        res: int = 0
        n: int = len(s)
        cache: Dict[str, int] = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev: int = 0
        j: int = n - 1
        while j > -1:
            el: str = s[j]
            val: int = cache[el]
            if val < prev:
                res -= val
            else:
                res += val
            prev = val
            j -= 1
        return res