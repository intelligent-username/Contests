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
        # Find the height of the tree
        h = 1
        current = root
        while root.left not None
            h += 1
            current = current.left
        
        big_list = []
        temp = []
        current = root

        for x in range(h):
            temp += current.value

            # VERY INCOMPLETE STOPPED HERE DUE TO BUSY


        return big_list