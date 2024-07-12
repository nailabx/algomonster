from typing import Deque
from collections import deque
class ReverseParentheses:
    def reverseParentheses(self, s: str) -> str:
        """
        You are given a string s that consists of lower case English letters and brackets.
        Reverse the strings in each pair of matching parentheses, starting from the innermost one.
        Your result should not contain any brackets.

        Example 1:
        Input: s = "(abcd)"
        Output: "dcba"
        Example 2:

        Input: s = "(u(love)i)"
        Output: "iloveu"
        Explanation: The substring "love" is reversed first, then the whole string is reversed.
        Example 3:

        Input: s = "(ed(et(oc))el)"
        Output: "leetcode"
        Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
        """
        stack: Deque = deque()
        for char in s:
            if char == ")":
                #process to reverse the element in the stack up to a open (
                toBeRev :str = ""
                while stack and stack[-1] != "(":
                    toBeRev += stack.pop()
                #Pop the the opening
                if stack and stack[-1] == "(":
                    stack.pop()
                for c in toBeRev:
                    stack.append(c)
            else:
                stack.append(char)
        return "".join(stack)




