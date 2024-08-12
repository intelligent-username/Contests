# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# Vertical Order Traversal of a Binary Tree
# Incomplete
# LOl completely misunderstood, it's passing a tree data type redo later

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
        layers = math.log(2, len(root) + 1)
        big_list = []

        for x in range(1, layers+1):
            x = 2^x
            temp_list = []
            for r in range(x):
                temp_list.append(root.pop())

            big_list += temp_list

        return big_list

