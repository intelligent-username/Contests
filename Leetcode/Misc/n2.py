# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = set()
        
        # First pass: mark unmatched closing brackets and keep track of opening brackets
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)
        
        # Add indices of unmatched opening brackets to the removal set
        to_remove = to_remove.union(set(stack))
        
        # Construct the final string
        result = []
        for i, char in enumerate(s):
            if i not in to_remove:
                result.append(char)
        
        return ''.join(result)