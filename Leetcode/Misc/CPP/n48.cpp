// https://leetcode.com/problems/reverse-linked-list-ii/

// Complete

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        // Reverse nodes from position left to position right of the linked list
        if (!head || left == right) return head;

        int p1 = 1;
        ListNode header(0, head);
        ListNode* prev = &header;

        // Get to position left
        while (p1 < left && prev->next != nullptr) {
            prev = prev->next;
            p1++;
        }

        ListNode* ptr = prev->next;
        ListNode* nxt;
        int p2 = p1;

        // Swap up to position right
        while (p2 < right) {
            p2++;
            nxt = ptr->next;
            ptr->next = nxt->next;
            nxt->next = prev->next;
            prev->next = nxt;
        }

        return header.next;
    }
};
