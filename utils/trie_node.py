from typing import Dict
class TrieNodeMap:
    def __init__(self) -> None:
        self.children: Dict[str, TrieNodeMap] = dict()

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def charToIndex(self, ch):
        # Convert character to index (0-25)
        return ord(ch) - ord('a')

    def insert(self, word):
        node = self.root
        for char in word:
            index = self.charToIndex(char)
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.isEndOfWord = True