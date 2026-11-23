// https://leetcode.com/problems/rotate-list/description/?envType=problem-list-v2&envId=two-pointers&utm_source=chatgpt.com

// Introduces Cycling :)

// COMPLETE

/**
 * Definition for singly-linked list.
**/

 struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        // We want to return the new head of the Linked list

        if (head == nullptr) return head;

        int len = 1;

        ListNode* p1 = head;

        // To help with wrapping around, find length.

        while (p1->next != nullptr) {
            len++;
            p1 = p1->next;
        }

        k %= len;

        if (k == 0) return head;

        // Actually, the challenge was going to be to wrap around, but if I just make the list circular

        p1->next = head;
        ListNode* p2 = head;

        // And shift where the head by k nodes

        for (int i = 0; i < len - k - 1; i++) {
            p2 = p2->next;
        }

        // Ensure p1 is the head
        p1 = p2->next;

        p2->next = nullptr;

        return p1;

    }
};
