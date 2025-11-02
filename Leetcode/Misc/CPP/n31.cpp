// https://leetcode.com/problems/swap-nodes-in-pairs/

// Complete

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
    ListNode* swapPairs(ListNode* head) {
        ListNode* temp = new ListNode();
        if(!head || !head->next) return head;
        
        ListNode* head1 = temp;
        ListNode* head2 = head;

        while (head2 && head2->next) {
            head1->next = head2->next;
            head2->next = head1->next->next;
            head1->next->next = head2;

            head1 = head2;
            head2 = head2->next;

        }

        return temp->next;

    }
};
