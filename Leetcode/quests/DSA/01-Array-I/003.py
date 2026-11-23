# https://leetcode.com/problems/max-consecutive-ones/
# Done
# Eaaaaaaaaaaaaaaaaaaasy

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        rec = 0
        curr = 0

        for i in nums:
            if i == 1:
                curr += 1
                rec = max(curr, rec)
            else:
                curr = 0
        
        return rec
