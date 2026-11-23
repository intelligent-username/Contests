# https://leetcode.com/problems/binary-tree-level-order-traversal-ii

# Complete

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        ans = []
        
        if not root:
            return ans

        curr = deque([root])

        while curr:
            tmp = []
            for x in range(len(curr)):
                c = curr.popleft()
                tmp.append(c.val)
                l = c.left
                r = c.right
                if l:
                    curr.append(l)
                if r:
                    curr.append(r)
            
            ans.append(tmp)

        return ans[::-1]
