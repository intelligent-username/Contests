# https://leetcode.com/problems/keep-multiplying-found-values-by-two/?envType=daily-question&envId=2025-11-19
# Crazy easy daily problem
# Complete

from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        track = set()
        for i in nums:
            track.add(i)

        while original in track:
            original *= 2
        return original
