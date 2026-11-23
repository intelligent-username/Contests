# https://leetcode.com/problems/linked-list-cycle-ii
# Complete

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        seen = set()
        curr = head
        
        # if curr.val is None or curr.next is None:
        #     return curr

        while curr:
            if curr in seen:
                return curr
            seen.add(curr)
            curr = curr.next
        return None
