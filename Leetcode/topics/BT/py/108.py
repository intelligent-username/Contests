# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Complete

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Ok, given a sorted array, convert it to a height-balanced Binary Search Tree
        # So that means middle item at the root

        # Huh this was actually easy
        
        if not nums:
            return None

        num = len(nums)
        half = num//2

        if num <= 1:
            return TreeNode(nums[0])

        return TreeNode(val=nums[half], left=self.sortedArrayToBST(nums[0:half]), right=self.sortedArrayToBST(nums[half+1:]))
