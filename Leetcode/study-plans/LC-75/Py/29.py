# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list

# Delete a node in the middle of a linked list
# Harder than t should be (I'm just lazy with the navigation)

# Complete

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        if not head.next:
            return None
        
        length = 0

        curr = head

        while curr:
            curr = curr.next
            length += 1
        
        cut = length // 2 - 1
        curr = head

        for _ in range(cut):
            curr = curr.next
        
        curr.next = curr.next.next

        return head
