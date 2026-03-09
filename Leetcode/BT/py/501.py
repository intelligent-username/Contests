# https://leetcode.com/problems/find-mode-in-binary-search-tree

# Complete

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        counts = {}
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            counts[node.val] = counts.get(node.val, 0) + 1
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            
        max_freq = max(counts.values())
        return [val for val, freq in counts.items() if freq == max_freq]
