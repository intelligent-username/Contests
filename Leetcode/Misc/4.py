# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        import collections
        node_list = []

        def dfs(node, row, col):
            if node:
                node_list.append((col, row, node.val))
                dfs(node.left, row + 1, col - 1)
                dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        node_list.sort()

        res = []
        prev_col = float('-inf')
        for col, row, value in node_list:
            if col != prev_col:
                res.append([])
                prev_col = col
            res[-1].append(value)
        return res
