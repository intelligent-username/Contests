# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number
# Done

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        # Was thinking of using a modified binary tree
        # But the range 0 <= i <= 100 gives this away.
        # I think we can call tihs an easy DP problem
        # Imma make a frequency list then use that to make a sum list

        freq = 101 * [0]

        sums = 101 * [0]
        n = len(nums)
        ans = [-1] * n

        for i in nums:
            freq[i] += 1

        sums[0] = 0

        for j in range(1, 101):
            sums[j] = sums[j-1] + freq[j-1]

        for j in range(n):
            ans[j] = sums[nums[j]]

        return ans
