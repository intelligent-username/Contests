# Second version

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
        
        self.max_freq = 0
        self.freq = {}
        self.modes = []

        def process(val: int):
            if val not in self.freq:
                self.freq[val] = 1
            else:
                self.freq[val] += 1
            
            if self.freq[val] > self.max_freq:
                self.max_freq = self.freq[val]
                self.modes = [val]
            elif self.freq[val] == self.max_freq:
                self.modes.append(val)
        
        def iot(src: Optional[TreeNode]):
            # In-order traversal
            if src.left:
                iot(src.left)
            process(src.val)
            if src.right:
                iot(src.right)
        
        iot(root)
        return self.modes

