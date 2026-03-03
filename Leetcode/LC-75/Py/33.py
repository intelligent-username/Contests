# https://leetcode.com/problems/maximum-depth-of-binary-tree

# Max Depth
# Starting DFS practice again. I've done this problem before but recursively in C++.

# Complete

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # if not root:
        #     return 0
        
        # # Realized thisi s redundant:
        #     # if not root.left and not root.right:
        #     #     return 1
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        if not root:
            return 0
        
        # Depth-first search, so using a stack.

        # LIFO
        # I'm using a deque just for 'practice'
        # But a list would be more efficient (push to and pop from the back)
        frontier = deque([(root, 1)])

        # This frontier declaration was causing issues
        # If passing an iterable to deque, it'll add the members of the iterable
        # INDIVIDUALLY to the deque
        # Same applies for lists, sets, and other iterable-like containers
        
        # Ok, I'll keep track of the item itself as well as its depth
        # Then process based on that
        # So we can infer the height of the childrne based on the height of the parents

        # No need for a visited set since this is a tree (no redundancy)

        maxheight = 1

        while frontier:
            curr = frontier.pop()
            node = curr[0]
            depth = curr[1]


            if depth >= maxheight:
                maxheight = depth

            if node.left:
                frontier.append((node.left, depth + 1))
            
            if node.right:
                frontier.append((node.right, depth + 1))
            
        return maxheight

