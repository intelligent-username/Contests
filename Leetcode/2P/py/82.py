# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# IDK why this is in the two pointer section but it is

# Complete

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Note: delete ALL nodes that have duplicate numbers, not JUST the duplicates
        # Also note that we're checking for duplicate *values*, not duplicate nodes
        # Forgot the list is sorted but whatever. T~oo late now

        # Ok, just keep track of how many occurances of each one
        seen = {}

        temp = head
        while temp:
            n = temp.val
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1
            temp = temp.next
        
        temp = ListNode(10)
        temp.next = head
        curr = temp

        # Then go delete all the ones with duplicates

        while curr.next:
            if seen[curr.next.val] > 1:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return temp.next


