// https://leetcode.com/problems/reverse-linked-list

// Reversing a linked list

// The bane of every CS student

// Complete

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }

        ListNode* curr1 = head;
        ListNode* curr2 = curr1->next;
        
        // Missing This was causing an infinite loop:
        curr1->next = nullptr;

        ListNode* temp;

        while (curr2->next) {
            temp = curr2->next;
            curr2->next = curr1;
            curr1 = curr2;
            curr2 = temp;
        }

        curr2->next = curr1;
        return curr2;

    }
};
