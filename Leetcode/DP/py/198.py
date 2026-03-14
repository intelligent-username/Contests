# https://leetcode.com/problems/house-robber/description/

# Complete

class Solution:
    def rob(self, nums: List[int]) -> int:
        vals = []
        
        n = len(nums)

        if n == 1:
            return nums[0]
        
        vals = [0] * n

        vals[0] = nums[0]
        vals[1] = max(nums[0], nums[1])

        # Len >= 2
        for i in range(2, n):
            vals[i] = max(
                vals[i-1], nums[i] + vals[i-2]
            )
        
        return vals[n-1]

