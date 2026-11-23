# https://leetcode.com/problems/set-mismatch/
# Done

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
 
        n = len(nums)
        founds = [0] * n

        ans = [0, 0]

        actual = 0
        expected = (n * (n + 1)) // 2

        for i in range(n):
            num = nums[i] - 1
            actual += nums[i]
            founds[num] += 1
            if founds[num] > 1:
                ans[0] = nums[i]

        # Ok I didn't think about figuring out which number is missing breh
        # If NONE were missing, the sum would be (n * (n+1)) // 2
        # But curr has the sum of all i in nums
        # So expected - actual = missing - duplicate

        # Ah ok so assign sum and expected easy

        ans[1] = expected - actual + ans[0]

        return ans
