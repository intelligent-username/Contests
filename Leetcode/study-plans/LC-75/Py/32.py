# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Complete

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        new = []

        curr = head
        while curr:
            new.append(curr.val)
            curr = curr.next
        
        # Guaranteed to be even btw
        length = len(new)
        int_max = float('-inf')
        for i in range(0, length // 2):
            q = new[i] + new[length- i - 1]
            if  q > int_max:
                int_max = q


        return int_max

        