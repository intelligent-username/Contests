# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k

# Complete

class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return True
        
        if 2 ** k > len(s):
            return False
        
        seq = set()

        # Just add every sequence to the set. This is brute force.
        # But remember it's ever set of LENGTH k, so it's a bit less repetitious.

        for i in range(len(s) - k + 1):
            seq.add(s[i:i+k])
        return len(seq) == 2**k