from typing import List, Dict, Tuple
import string

class Combinatory:

    KEYBORD: Dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

    """
    Given a non-negative integer n, find all n-letter words composed by 'a' and 'b', return them in a list of strings in lexicographical order.
    """
    def form_words(self, n: int)->List[str]:
        def dfs(index: int, path: List[str], res: List[str])->None:
            if index == n:
                res.append("".join(path))
                return
            for el in "a", "b":
                path.append(el)
                dfs(index + 1, path, res)
                path.pop()
        res = []
        dfs(0, [], res)
        return res
    
    def letter_combinations_of_phone_number(self, digits: str) -> List[str]:
        
        res = []
        def dfs(index, combo: List[str])->None:
            if index == len(digits):
                res.append("".join(combo))
                return
            letters = self.KEYBORD[digits[index]]
            for letter in letters:
                combo.append(letter)
                dfs(index + 1, combo)
                combo.pop()
        dfs(0, [])
        return res
    
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        def isPalindrome(s: str)->bool:
            return s[::-1]==s
        def dfs(start: int, path: List[str])->None:
            if start == n:
                res.append(path[:])
                return
            for end in range(start + 1, n + 1):
                prefix = s[start:end]
                if isPalindrome(prefix):
                    dfs(end, path + [prefix])
        dfs(0, [])
        return res
    
    def parentheses(self, n: int) -> str:
        res = []
        def dfs(index: int, path: List[str], open: int, close: int)->None:
            if index == 2*n:
                res.append("".join(path))
                return
            if open < n:
                path.append("(")
                dfs(index + 1, path, open + 1, close)
                path.pop()
            if close < open:
                path.append(")")
                dfs(index + 1, path, open, close + 1)
                path.pop()
        dfs(0, [], 0, 0)
        return res
    
    def decode_ways(self, digits: str) -> Tuple:
        map_letter: Dict[str, str] = {str(ord(a) - 64): a for a in string.ascii_uppercase}
        res = []
        def dfs(index: int, path: List[str]):
            if index == len(digits):
                res.append("".join(path))
                return 1
            ways = 0
            if digits[index] == "0":
                return ways
            path.append(map_letter[digits[index]])
            ways += dfs(index + 1, path)
            if 10 <= int(digits[index:index + 2]) <= 26:
                ways += dfs(index + 2, path)
            path.pop()
            return ways
        return res, dfs(0, [])
    
    def coin_change(self, coins: List[int], amount: int)->Tuple:
        res = []
        n = len(coins)
        def dfs(start: int, left: int, path: List[int])->None:
            if left == 0:
                res.append(path[:])
                return
            for i in range(start, n):
                coin = coins[i]
                if coin > left:
                    continue
                dfs(i, left - coin, path + [coin])
                # path.pop()
        dfs(0, amount, [])
        ans = len(sorted(res, key=len, reverse=False)[0]) if res else -1
        return res, ans
    def three_sums(self, nums: List[int], target: int)->List[int]:
        nums.sort()
        n = len(nums)
        res = []
        def two_sums(nums: List[int], target: int)->List[int]:
            #Nums need to be sorted
            l, r = 0, len(nums) - 1
            while l <= r:
                total = nums[l] + nums[r]
                if total > target:
                    r -= 1
                elif total < target:
                    l -= 1
                else:
                    return [nums[l], nums[r]]
            return []
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]: continue
            ts = two_sums(nums[i+1:], target - nums[i])
            total = nums[i] + sum(ts)
            if total == target:
                res.append([nums[i]] + ts)
        return res
    
    def valid_parentheses(self, s: str)->List[str]:
        pass

    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def to_ip_address(path):
            address = path[0]
            for i in range(1, 4): address += "." + path[i]
            return address
        
        def get_edges(index):
            segments = []
            for i in range(index, index + 3):
                if i < len(s) :    
                    segments.append(s[index:i+1])
            return segments
        
        def is_valid(num):
            if num == "0": return True
            elif num[0] == "0": return False    # leading zero
            elif int(num) > 255: return False   # out of range
            else: return True
        def dfs(index, path):
            if len(path) > 4: return
            if index == len(s):   # if all digits are used
                if len(path) == 4:      # and there are exactly four segments
                    ans.append(to_ip_address(path))     # add address to the result
                return
            for edge in get_edges(index):
                if is_valid(edge):
                    path.append(edge)
                    dfs(index + len(edge), path)
                    path.pop()
        # print(s[0:len(s)+1])
        dfs(0, [])
        return ans


