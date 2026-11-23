# https://leetcode.com/problems/odd-even-linked-list/
# Had to draw this out but otherwise it was fine

# Complete

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Odd INDICES need to be grouped with odd Indices
        # then EVEN indices with even indices

        if not head or not head.next:
            return head
        
        odd = head
        evenHead = odd.next
        even = evenHead

        while even and even.next:

            odd.next = odd.next.next
            even.next = odd.next.next
            
            odd = odd.next
            even = even.next

        odd.next = evenHead
        return head