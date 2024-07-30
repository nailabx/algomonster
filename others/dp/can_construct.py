from typing import List, Dict
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False

class CheckCanConstruct:
    # def canConstrcut(self, target: str, words: List[str])->bool:
    #     trieNode: TrieNode = TrieNode()
    #     for w in words:
    #         node = trieNode
    #         for e in w:
    #             if not node.children[ord(e) - ord("a")]:
    #                 node.children[ord(e) - ord("a")] = TrieNode()
    #             node = node.children[ord(e) - ord("a")] 
    #         node.endOfWord = True
        
    #     def dfs(target: str, trie: TrieNode, curr: str)->None:
    #         if curr == target:
    #             return True
            
    #         for i in range(len(target)):
    #             prefix = target[:i]

    def canConstruct(self, target: str, words: List[List[str]], memo: Dict = {})->bool:
        if target in memo:
            return memo[target]
        if target == "":
            return True
        for word in words:
            if target and target.startswith(word):
                suffix: str = target[len(word):]
                memo[suffix] =  self.canConstruct(suffix, words)
                if memo[suffix]: 
                    return True
        memo[target] = False
        return memo[target]
    
    def canConstructTab(self, target: str, words: List[List[str]])->bool:
        tab: List[str] = [False] * (len(target) + 1)
        tab[0] = True
        for i in range(len(target) + 1):
            if tab[i]:
                for w in words:
                    if target[i:i + len(w)] == w:
                        tab[i + len(w)] = True
        print(tab)
        return tab[len(target)]

    

if __name__ == "__main__":
    target:str = "abcdef"
    words:List[str] = ["ab", "abc", "cd", "def", "abcd"]
    c = CheckCanConstruct()
    print(c.canConstructTab(target, words))


        
            
