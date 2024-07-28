from unittest import TestCase
from others.dp.fibonacci import Solution
class TestFibonnaci(TestCase):

    def test_fibonnaci(self):
        self.fib = Solution()
        n: int = 10
        print(self.fib.fibonnaciMemo(n=n))
        