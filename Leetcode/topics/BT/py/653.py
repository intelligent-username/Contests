# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

# Complete

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        vals = set()

        queue = deque([root])

        while queue:
            x = queue.popleft()
            if (k - x.val) in vals:
                return True
            else:
                vals.add(x.val)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)


        return False
        
