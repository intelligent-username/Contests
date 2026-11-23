# https://leetcode.com/problems/balanced-binary-tree

# Complete

import math
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return abs(self.dfs(root.left) - self.dfs(root.right)) <= 1
        

    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return 0
        else:
            lft = self.dfs(root.left)
            rgt = self.dfs(root.right)
            if abs(lft - rgt) <= 1:
                # 
                return 1 + max(lft, rgt)
            else:
                return math.inf
