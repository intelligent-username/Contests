# https://leetcode.com/problems/balance-a-binary-search-tree/

# Complete

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None
        
        # Tbh we're best off just constructing it

        ans = []

        def trav(node):
            if not node: 
                return None
            
            trav(node.left)
            ans.append(node)
            trav(node.right)
        
        def build(start, end):

            if start > end:
                return None

            m = (start + end) // 2
            root = ans[m]
            root.left = build(start, m-1)
            root.right = build(m+1, end)

            return root
        
        trav(root)
        return build(0, len(ans) - 1)
