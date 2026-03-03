# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Complete

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        def helper(prefix, rem_digs):
            """
            Prefix is all the ones that are preceeding it
            digits are the remaining digits
            """
            if not rem_digs:
                possibilities.append(prefix)
                return
            
            else:
                first = rem_digs[0]
                for letter in keys[first]:
                    helper(prefix + letter, rem_digs[1:])

        keys = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl",
                '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

        possibilities = []

        # Looks like I'm going to have to recurse

        helper("", digits)

        return possibilities
