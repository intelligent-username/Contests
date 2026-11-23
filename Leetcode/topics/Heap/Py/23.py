# https://leetcode.com/problems/merge-k-sorted-lists/

# Basically a free easy problem

# Complete

from typing import List, Optional
from heapq import heapify, heappop, heappush
from itertools import count

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        # First idea is to just look at the earliest member of each list and always select the minimum, making it the next.
        # But that'd have a few layers of hard-to-follow for loops
        # Also, select the earliest member every time sounds like a heap.
        # What if I create a min-heap sorted based on value.
        # Oh then constantly pop the min value and make the popped item self.next
        # Ok. Also, without the heap it would require len(lists) comparisons every time
        # So we're not wasting anything by creating the heap
        # But ALSO, because the heap is created and we're using extra space we don't need the lists to all be sorted.

        lst = []
        ctr = count()

        for i in lists:
            if i:
                lst.append((i.val, next(ctr), i))
        
        heapify(lst)

        # Apparantly the list itself can be non-empty by only containing empty sublists :(
        if not lst:
            return None

        root = heappop(lst)[2]
        curr = root

        if curr.next:
            heappush(lst, (curr.next.val, next(ctr), curr.next))

        while lst:
            curr.next = heappop(lst)[2]
            curr = curr.next
            if curr.next:
                heappush(lst, (curr.next.val, next(ctr), curr.next))

        return root
