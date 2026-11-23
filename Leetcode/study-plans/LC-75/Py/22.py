# https://leetcode.com/problems/determine-if-two-strings-are-close

# Determine if two strings are close

# Complete
# Beats 89.54% of Python submissions !?
# Not that these numbers are accurate

class Solution(object):
    def closeStrings(self, word1, word2):
        if len(word1) != len(word2):
            return False

        map1 = {}
        cc1 = []
        cs1 = set()
        for c in word1:
            if c in map1:
                map1[c] += 1
            else:
                map1[c] = 1

        map2 = {}
        cc2 = []
        cs2 = set()
        for c in word2:
            if c in map2:
                map2[c] += 1
            else:
                map2[c] = 1

        for key, val in map1.items():
            cs1.add(key)
            cc1.append(val)

        for key, val in map2.items():
            cs2.add(key)
            cc2.append(val)

        cc1.sort()
        cc2.sort()

        return cs1 == cs2 and cc1 == cc2
