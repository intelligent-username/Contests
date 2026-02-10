# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced

# Complete

class Solution:
    def minimumDeletions(self, s: str) -> int:
        # a = 0
        b = 0

        cost = 0

        # All 'a's must come before all 'b's

        # Not all 'b's must be matched with a previous 'a'

        for c in s:
            if c == 'b':
                b += 1
            elif c == 'a':
                cost = min(cost + 1, b)
        
        return min(cost, b)
