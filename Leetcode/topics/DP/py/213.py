# https://leetcode.com/problems/house-robber-ii/description/

# Completed but kind of BS

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f = nums[0]
        
        if n == 1: return f

        s = nums[1]

        if n == 2: return max(f, s)
        
        maxs = [0] * n
        maxs[0] = f
        maxs[1] = max(f, s)

        for i in range(2, n-1):
            maxs[i] = max(
                maxs[i - 1], maxs[i - 2] + nums[i]
            )
        
        # The one problem is, the first house is adjacent to the last house...

        maxs2 = [0] * n
        maxs2[1] = nums[1]
        maxs2[2] = max(s, nums[2])

        for i in range(3, n):
            maxs2[i] = max(
                maxs2[i - 1], maxs2[i - 2] + nums[i]
            )
        
        return max(
            maxs[n-2], maxs2[n-1]
        )
