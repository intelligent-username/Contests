# https://leetcode.com/problems/sum-of-left-leaves

# Complete

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return  0

        if not root.left and not root.right:
            return 0
        
        currs = deque([root])

        total = 0 

        while currs:
            curr = currs.popleft()

            l = curr.left

            if l:
                if not l.left and not l.right:
                    total += l.val
                currs.append(l)
            
            if curr.right:
                currs.append(curr.right)
        
        return total
