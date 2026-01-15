# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Complete

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        curr = [root]
        nxt = []

        rev = False
        
        while curr:
            tmp = []
            for x in curr:
                tmp.append(x.val)
                if x.left:
                    nxt.append(x.left)
                if x.right:
                    nxt.append(x.right)
            if rev:
                tmp.reverse()
                rev = False
            else:
                rev = True
            ans.append(tmp)
            
            curr = nxt
            nxt = []
            temp = []

        return ans
            
