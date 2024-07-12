from typing import Tuple, Deque
from collections import deque

class MaxScoreRemoveSubstring:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        """
        You are given a string s and two integers x and y. You can perform two types of operations any number of times.
        Remove substring "ab" and gain x points.
        For example, when removing "ab" from "cabxbae" it becomes "cxbae".
        Remove substring "ba" and gain y points.
        For example, when removing "ba" from "cabxbae" it becomes "cabxe".
        Return the maximum points you can gain after applying the above operations on s.
        """

        def remove(s: str, first: str, second: str, point: int)->Tuple[str, int]:
            stack: Deque = deque()
            score: int = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    score += point
                    stack.pop()
                else:
                    stack.append(char)
            return "".join(stack), score
        if x > y:
            s, score1 = remove(s, "a", "b", x)
            s, score2 = remove(s, "b", "a", y)
        else:
            s, score1 = remove(s, "b", "a", y)
            s, score2 = remove(s, "a", "b", x)
        return score1 + score2

            