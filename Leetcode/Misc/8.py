# Problem #1234, medium
# https://leetcode.com/problems/replace-the-substring-for-balanced-string/

from collections import Counter

class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s) # Get the total & of characters
        
        avg = n // 4 # This is "how" it'l balance.
        cnt = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        for ch in s:
            cnt[ch] += 1

        need = {c: max(0, cnt[c] - avg) for c in "QWER"}
        if all(v == 0 for v in need.values()):
            return 0 # Already balanced

        res = n
        l = 0
        for r, ch in enumerate(s):
            need[ch] -= 1
            while l <= r and all(v <= 0 for v in need.values()):
                res = min(res, r - l + 1)
                need[s[l]] += 1
                l += 1

        return res
