# https://leetcode.com/problems/invert-binary-tree/description

# Complete

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return root


        currs = [root]
        nexts = []

        while currs:
            for x in currs:
                x.left, x.right = x.right, x.left
                if x.left:
                    nexts.append(x.left)
                
                if x.right:
                    nexts.append(x.right)
            
            currs = nexts
            nexts = []
        
        return root
