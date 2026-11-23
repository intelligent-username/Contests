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
        
        # Honestly, best off just straight up constructing it
        # Since it's a BST, it's alraedy in order
        # Just do in-order traversal, that'll append smallest -> biggest

        ans = []

        # Passing 'ans' around is SLIGHTLY faster
        # But not necessary
        def trav(node, ans):
            if not node: 
                return None

            trav(node.left, ans)
            ans.append(node)
            trav(node.right, ans)
        
        def build(start, end, ans):

            if start > end:
                return None

            m = (start + end) // 2
            root = ans[m]
            root.left = build(start, m-1, ans)
            root.right = build(m+1, end, ans)

            return root
        
        trav(root, ans)
        return build(0, len(ans) - 1, ans)
