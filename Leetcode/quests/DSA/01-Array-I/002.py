# https://leetcode.com/problems/shuffle-the-array/
# Done
# Again very easy
# This is starting to make me feel goo about myself lol

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # Ok given nums of length 2n
        # For i in n:
            # Put nums[i+n] after it
        
        # Ok this can be done in linear time easily
        # We're working with arrays
        # So I don't think i can speed it up any more
        # Like there's no data structure-based shortcut.
        # I was thinking of doing swaps but that's also linear.

        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])

        return ans
