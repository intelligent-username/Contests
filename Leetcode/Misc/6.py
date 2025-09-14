# https://leetcode.com/problems/palindrome-number/
# Check if a number is palindrome
# Clasically EASY Python Implementation

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        x2 = x[::-1]
        return x2 == x
