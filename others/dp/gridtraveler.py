from typing import Dict, List

class GridTraveler:
    def tabtravel(self, n:int, m:int)->int:
        if n == 0 or m == 0:
            return 0
        tab: List[List[int]] = [[0]*(m + 1) for _ in range(n + 1)]
        tab[1][1] = 1
        for r in range(n + 1):
            for c in range(m + 1):
                current: int = tab[r][c]
                if r + 1 <= n: tab[r + 1][c] += current
                if c + 1 <= m: tab[r][c + 1] += current
                # tab[r][c] = tab[r-1][c] + tab[r][c-1]
        return tab[n][m] 

    def travel(self, n: int, m: int, memo: Dict = {}):
        if n == 1 and m == 1:
            return 1
        
        if n == 0 or m == 0:
            return 0
        
        if (n, m) in memo:
            return memo[(n, m)]
        
        memo[(n, m)] = self.travel(n - 1, m) + self.travel(n, m - 1)
        return memo[(n, m)]
    
if __name__ == "__main__":
    g = GridTraveler()
    print(g.tabtravel(18, 18))
    print(g.travel(18, 18))