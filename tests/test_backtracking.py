import unittest
from dsa.backtracking.combinatory import Combinatory

class BacktrackingTest(unittest.TestCase):
    def setUp(self) -> None:
        self.bt = Combinatory()
    
    def test_letter_combo(self):
        n: int = 3
        res = self.bt.form_words(n)
        self.assertEqual(len(res), 8)    
    def test_letters_digit(self):
        digits = "565"
        res = self.bt.letter_combinations_of_phone_number(digits)
        self.assertTrue("jmj" in set(res))
        # print(self.bt.KEYBORD)
        # print(res)
    
    def test_parentheses(self):
        n: int = 4
        res = self.bt.parentheses(n)
        self.assertIsNotNone(res)
    
    def test_ways_to_decode(self):
        digits: str = "27"
        res = self.bt.decode_ways(digits)
        self.assertIsNotNone(res)
    
    def test_coins_change(self):
        coins, amount = [1, 2, 5], 11
        res = self.bt.coin_change(coins, amount)
        self.assertIsNotNone(res)

    def test_three_sum(self):
        nums, target = [3,1,1,2, 6], 6
        res = self.bt.three_sums(nums, target)
        # print(res)
    
    def test_restoreIpAddresses(self):
        s: str = "101023"
        res = self.bt.restoreIpAddresses(s)
        print(res)
    