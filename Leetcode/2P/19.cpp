// https://leetcode.com/problems/remove-nth-node-from-end-of-list/
// Complete

using namespace std;

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // "Follower" pointer
        ListNode* follower = head;
        ListNode* origHead = head; // store original head

        for (int i = 0; i < n; i++) {
            head = head->next;
        }

        if (!head) { // n == length of list, remove head
            return origHead->next;
        }

        while (head->next != nullptr) {
            head = head->next;
            follower = follower->next;
        }

        follower->next = follower->next->next;

        return origHead; // return full modified list starting from original head
    }
};
