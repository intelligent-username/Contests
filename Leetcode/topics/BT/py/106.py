# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

# Complete

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # The last item in postorder is the root.
        if not inorder: return None
        
        if len(inorder) == 1: return TreeNode(postorder[0])
        
        r = postorder[-1]
        m = inorder.index(r)

        root = TreeNode(r)
        # Oh and anything to the left of the root in inorder is the left subtree
        # Same as problem 105

        il = inorder[:m]
        ir = inorder[m + 1:]

        pl = postorder[:len(il)]
        pr = postorder[len(il):-1]

        root.left = self.buildTree(il, pl)
        root.right = self.buildTree(ir, pr)

        return root
