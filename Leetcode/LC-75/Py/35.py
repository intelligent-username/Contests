# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Complete

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        frontier = deque()
        frontier.append((root, root.val))

        num = 0

        # At each root, store the max of the max so far and it's value
        # So it's like a hereditary check
        # This pretty obviously looks right recursively

        while frontier:
            node, max_so_far = frontier.pop()

            if node.val >= max_so_far:
                num += 1

            new_max = max(max_so_far, node.val)

            if node.left:
                frontier.append((node.left, new_max))
            if node.right:
                frontier.append((node.right, new_max))

        return num

