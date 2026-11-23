# https://leetcode.com/problems/binary-tree-level-order-traversal

# Complete

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # Highest to lowest,
        # Left to right
        if not root:
            return []

        orders = []
        curr = [root]

        while curr:
            currvals = []
            nxt = []

            for x in curr:
                if x.val is not None:
                    currvals.append(x.val)
                    if x.left:
                        nxt.append(x.left)
                    if x.right:
                        nxt.append(x.right)
            orders.append(currvals)
            curr = nxt
        
        return orders


    # def bfs(self, root):
    #     pass
