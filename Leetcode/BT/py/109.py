# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree

# Complete

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return head
        
        if not head.next:
            return TreeNode(head.val)
        
        lag = None
        p1 = head
        p2 = head

        while p2 and p2.next:
            lag = p1
            p1 = p1.next
            p2 = p2.next.next
        
        lag.next = None

        root = TreeNode(p1.val)

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(p1.next)

        return root


