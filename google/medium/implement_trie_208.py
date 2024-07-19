from utils.trie_node import TrieNode
class ImplementTrie:
    def __init__(self):
        self.root: TrieNode = TrieNode()
        

    def insert(self, word: str) -> None:
        curr: TrieNode = self.root
        for w in word:
            idx: int = ord(w) - ord("a")
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.endOfword = True
        

    def search(self, word: str) -> bool:
        node: TrieNode = self.root
        for w in word:
            idx: int = ord(w) - ord("a")
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return node.endOfword
        

    def startsWith(self, prefix: str) -> bool:
        node: TrieNode = self.root
        for w in prefix:
            idx: int = ord(w) - ord("a")
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return True
