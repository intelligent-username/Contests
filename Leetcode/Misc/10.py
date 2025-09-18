# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # eaaaaaaasy just for fun
        if not nums:
            return 0

        i = 0  # pointer to last unique element

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]  # overwrite next spot with new unique

        return i + 1  # number of unique elements
