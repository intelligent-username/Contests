# https://leetcode.com/problems/populating-next-right-pointers-in-each-node

# Complete

from collections import deque
from typing import Optional

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        curr = deque([root])
        nexts = deque()

        while curr:
            while curr:
                x = curr.popleft()
                if len(curr) > 0:
                    x.next = curr[0]
                if x.left:
                    nexts.append(x.left)
                if x.right:
                    nexts.append(x.right)
            
            curr = nexts
            nexts = deque()


        return root
