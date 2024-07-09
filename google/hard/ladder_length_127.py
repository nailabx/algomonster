from typing import List, Iterator, Deque
from collections import deque
from string import ascii_letters
class WordladderLength:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        
        queue = deque([(beginWord, 1)])
        
        while queue:
            curr, count = queue.popleft()
            if curr == endWord:
                return count
            for i in range(len(curr)):
                for c in ascii_letters:
                    x = curr[:i] + c + curr[i+1:]
                    if x in wordList:
                        queue.append((x, count + 1))
                        wordList.remove(x)
        
        return 0

