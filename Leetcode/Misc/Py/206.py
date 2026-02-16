# https://leetcode.com/problems/reverse-linked-list/

# Inefficient but just the first thing that came to mind

# Complete


import deque
from typing import Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        rev = deque()

        while head:
            rev.append(head)
            head = head.next

        new = rev.pop()
        curr = new

        while rev:
            curr.next = rev.pop()
            curr = curr.next

        curr.next = None
        return new
