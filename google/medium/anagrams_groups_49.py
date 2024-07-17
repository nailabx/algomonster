from typing import List, Dict
from collections import defaultdict
class AnagramGroup:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res: Dict[str, List[str]] = defaultdict(list)
        for string in strs:
            letters: List[str] = [0] * 26
            for letter in string:
                letters[ord(letter) - ord("a")] += 1
            res[tuple(letters)].append(string)
        return res.values()
