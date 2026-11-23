# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Done

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)

        freq = [0] * (n)

        for i in nums:
            freq[i - 1] += 1

        ans = []
        for i in range(n):
            if freq[i] == 0:
                ans.append(i + 1)

        return ans
