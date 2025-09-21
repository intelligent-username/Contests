# https://leetcode.com/problems/length-of-last-word/description/
# Given a string s consisting of words and spaces, return the length of the last word in the string.


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        Note: strings will only contain English words and spaces. So no need to worry about commas, etc.
        At least in this problem :)
        """
        temp = s.split()
        return len(temp[-1])
        