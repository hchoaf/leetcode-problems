# link: https://leetcode.com/problems/valid-parentheses/submissions/

# Given a string of parantheses, check if it is valid (matching)

from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque([])
        
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if stack:
                    if c == ')':
                        if stack.pop() != '(':
                            return False
                    elif c == ']':
                        if stack.pop() != '[':
                            return False
                    elif c == '}':
                        if stack.pop() != '{':
                            return False
                else:
                    return False
        if stack:
            return False
        return True
        
        