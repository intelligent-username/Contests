# https://leetcode.com/problems/recover-binary-search-tree

# Complete  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        p1 = None
        p2 = None

        def inorder(node):
            nonlocal prev, p1, p2
            if not node:
                return
            
            inorder(node.left)

            if prev and prev.val > node.val:
                if not p1:
                    p1 = prev
                p2 = node

            prev = node

            inorder(node.right)
        
        if not root:
            return root
        
        inorder(root)
        p1.val, p2.val = p2.val, p1.val
        return root
