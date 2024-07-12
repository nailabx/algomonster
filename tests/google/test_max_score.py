from unittest import TestCase
from google.medium.max_score_remove_substring_1717 import MaxScoreRemoveSubstring

class TestMaxScoreRemoveSubstring(TestCase):

    def setUp(self) -> None:
        self.score = MaxScoreRemoveSubstring()
    
    def test_max_score_remove_substring(self):
        s: str = "cdbcbbaaabab"
        res = self.score.maximumGain(s=s, x=4, y=5)
        self.assertEqual(res, 19)