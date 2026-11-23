# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii

# Complete

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        curr = deque([root])
        nexts = deque()

        while curr:
            while curr:
                x = curr.popleft()
                if curr:
                    x.next = curr[0]
                
                l = x.left
                r = x.right
                if l:
                    nexts.append(l)
                if r:
                    nexts.append(r)
            curr = nexts
            nexts = deque()
        
        return root
