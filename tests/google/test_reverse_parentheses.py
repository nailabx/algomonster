from unittest import TestCase
from google.medium.reverse_parentheses_1190 import ReverseParentheses

class TestReverseParentheses(TestCase):

    def setUp(self) -> None:
        self.p :ReverseParentheses = ReverseParentheses()
    

    def test_reverse_parentheses(self):
        s: str = "(ed(et(oc))el)"
        res: str = self.p.reverseParentheses(s=s)
        print(res)
