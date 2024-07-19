from typing import List, Dict
from collections import defaultdict
class TrieNode:
    def __init__(self, weight: int = 0):
        self.children: List[str] = [None]*26
        self.weight: int = weight

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.map: Dict = defaultdict(int)
        

    def insert(self, key: str, val: int) -> None:
        newVal: int = val - self.map.get(key, 0)
        self.map[key] = val
        node: TrieNode = self.root
        node.weight += newVal
        for w in key:
            idx: int = ord(w) - ord("a")
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
            node.weight += newVal
        

    def sum(self, prefix: str) -> int:
        node: TrieNode = self.root
        for w in prefix:
            idx: int = ord(w) - ord("a")
            if not node.children[idx]:
                return 0
            node = node.children[idx]
            
        return node.weight
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)