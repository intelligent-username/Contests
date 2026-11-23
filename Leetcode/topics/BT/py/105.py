# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Complete

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Aight so we can construct many possible binary trees
        # But since we're given both pre-order and post-order, a SPECIFIC binary tree is described
        # It's not a BST

        # I'm thinking use preorder to construct "naively" except check the inorder to ensure that the "preorder" neighbuours are also neighbors in preorder to ensure that they're actually children.

        if preorder == []:
            return None
        
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        root = TreeNode(preorder[0])
        # Anything to the left of root in inorder is in the left subtree
        # Anything to the right will be found in the right subtree

        # Oh ok just recurse on left and right

        mid = inorder.index(preorder[0])

        left_in = inorder[:mid]
        right_in = inorder[mid + 1:]

        left_pre = preorder[1:1 + len(left_in)]
        right_pre = preorder[1 + len(left_in):]

        root.left = self.buildTree(left_pre, left_in)

        # ...

        root.right = self.buildTree(right_pre, right_in)

        return root