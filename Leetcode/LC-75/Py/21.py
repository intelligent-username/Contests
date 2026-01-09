# https://leetcode.com/problems/unique-number-of-occurrences

# Unique number of occurrences

# Complete

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        maps = {}
        for x in arr:
            if x in maps:
                maps[x] += 1
            else:
                maps[x] = 1
        
        counts = set()

        for val in maps.values():
            if val in counts:
                return False
            counts.add(val)
        
        return True
