# https://leetcode.com/problems/search-in-a-binary-search-tree/

# Complete

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if root.val == val:
            return root
        elif root.val > val:
            if root.left:
                return self.searchBST(root.left, val)
            return None
        else:
            if root.right:
                return self.searchBST(root.right, val)
            return None
