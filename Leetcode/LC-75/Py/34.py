# https://leetcode.com/problems/leaf-similar-trees

# Complete

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """

        # Ok so we're checking if the left-to-right sequence of the leaf nodes of two trees is the same
        # Time will be at least O(n) 
        #       (need to iterate through the entirety of each tree once.
        # O(logn) space since there will be that meany leaves in each tree.
        # No other way to do it that would be more efficient, I don't think.

        # Ok so simply do in-order traversal and when detecting a leaf node, add it
        if not root1 and not root2:
            return True

        elif not root1 or not root2:
            return False
        
        ls1 = []
        ls2 = []

        #  ...
        
        frontier = deque()
        
        frontier.append(root1)

        while frontier:
            curr = frontier.pop()

            if curr.right:
                frontier.append(curr.right)
            
            if curr.left:
                frontier.append(curr.left)
            
            if not curr.left and not curr.right:
                # Then not curr.left and not curr.right
                # I.e. both are none and it's a leaf
                ls1.append(curr.val)
            
        frontier.append(root2)

        while frontier:
            curr = frontier.pop()

            if curr.right:
                frontier.append(curr.right)
            
            if curr.left:
                frontier.append(curr.left)
            
            if not curr.left and not curr.right:
                ls2.append(curr.val)
            

        #  ...

        return ls1 == ls2

