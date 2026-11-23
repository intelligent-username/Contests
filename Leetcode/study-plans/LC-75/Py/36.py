# https://leetcode.com/problems/path-sum-iii/

# Complete

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        # If reachable: there's only one way to reach each node from any other node
        # Just need to keep track of every possible sum
        #           From every possible way of reaching a node

        def DFS(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            cnt = totals.get(curr_sum - targetSum, 0)
            
            totals[curr_sum] = totals.get(curr_sum, 0) + 1
            cnt += DFS(node.left, curr_sum)
            cnt += DFS(node.right, curr_sum)
            
            totals[curr_sum] -= 1

            return cnt

        if not root:
            return 0
        
        totals = {0: 1}
        
        return DFS(root, 0)
