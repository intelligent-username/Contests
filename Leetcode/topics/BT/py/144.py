# https://leetcode.com/problems/binary-tree-preorder-traversal/

# This really should've been put first in the LC Binary Tree playlist but whatever
# Only did this to brush up, since BFS/DFS are coming up in a course

# Complete

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []
        nexts = [root]

        while nexts:
            node = nexts.pop()
            ans.append(node.val)
            
            # Push right first so left is processed first
            if node.right:
                nexts.append(node.right)
            if node.left:
                nexts.append(node.left)

        return ans
