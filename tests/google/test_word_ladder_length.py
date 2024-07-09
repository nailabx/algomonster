import unittest
from google.hard.ladder_length_127 import WordladderLength
class TestWordladderLength(unittest.TestCase):

    def setUp(self) -> None:
        self.w = WordladderLength()

    def test_word_ladder(self):
        start: str = "hit"
        end: str = "cog"
        wordList: list[str] = ["hot","dot","dog","lot","log","cog"]
        self.w.ladderLength(start, end, wordList)
    
    def test_word_ladder_2(self):
        start = "COLD"
        end = "WARM"
        word_list = ["COLD", "GOLD", "CORD", "SOLD", "CARD", "WARD", "WARM", "TARD"]
        self.w.ladderLength(start, end, word_list)
