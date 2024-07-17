from typing import List, Dict
from collections import defaultdict, Counter
class TopKFrequent:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n: int = len(nums)
        counts: Dict[int, int] = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        top: List[List[int]] = [[] for _ in n +  1]

        for num, cnt in counts.items():
            top[cnt].append(num)
        
        res: List[int] = []
        for arr in counts:
            for el in arr:
                res.append(el)
                if len(res) == k:
                    return res
        return res
    
    def topKFrequentShort(self, nums: List[int], k: int) -> List[int]:
        counts: Dict = Counter(nums)
        res: List[int] = []
        for el, _ in counts.most_common(k):
            res.append(el)
        return res

