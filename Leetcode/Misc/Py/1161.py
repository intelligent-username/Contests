# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# Daily problem

# Complete

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Return the level with the highest sum

        # The sum of level 1 is the value of the root
        # The sum of level 2 is the sum of the children of all the ones in level 1.
        # The sum of level 3 is the sum of all the children of all the nodes in level 2
        # ... sum of level n is the num of all the children of all the nodes in level n-1


        maxint = float('-inf')
        maxloc = 0

        ind = 0

        currs = [root]

        next = []

        while currs != []:
            ind += 1
            temp = 0
            for x in currs:
                if x is not None:
                    temp += x.val
                    if x.left is not None:
                        next.append(x.left)
                    if x.right is not None:
                        next.append(x.right)
            
            if temp > maxint:
                maxint = temp
                maxloc = ind

            currs = next
            next = []
        

        return maxloc
