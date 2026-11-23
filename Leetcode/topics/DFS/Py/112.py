# https://leetcode.com/problem-list/depth-first-search/
# Complete

# Path Sum. Light

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        #  In case
        if not root:
            return False

        # DFS: keeps going until we find a leaf

        return self.dfs(root, targetSum)
        
        
    def dfs(self, node, diff):
        # In case
        if not node:
            return False

        diff -= node.val

        # If we're at a leaf, return true if adds up properly
        if not (node.left or node.right):
            return (diff == 0)
        
        return self.dfs(node.left, diff) or self.dfs(node.right, diff)
