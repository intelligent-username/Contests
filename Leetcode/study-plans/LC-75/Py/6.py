# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75
# Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        reverse = ""
        for x in range(len(temp)-1, -1, -1):
            reverse += temp[x]
            reverse += " "
        reverse = reverse[:-1]
        return reverse
    