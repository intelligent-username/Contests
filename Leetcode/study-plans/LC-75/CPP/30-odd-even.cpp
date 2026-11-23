// https://leetcode.com/problems/odd-even-linked-list

// C++ version

// Complete


/**
 * Definition for singly-linked list.
 */ 
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        // Will do this now in C++ and see how quickly I can finish it

        if (!head || !head->next) {
            return head;
        }

        ListNode* odd = head;
        ListNode* evenHead = odd->next;
        ListNode* even = evenHead;

        while (even && even->next) {
            odd->next = odd->next->next;
            even->next = even->next->next;

            odd = odd->next;
            even = even->next;

        }

        odd->next = evenHead;

        return head;

    }
};
