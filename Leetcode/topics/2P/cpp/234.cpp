// https://leetcode.com/problems/palindrome-linked-list/
// Complete
// Easy problem but I need it to rebuild the habit again.

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    bool isPalindrome(ListNode* head) {
        // This is a two pointer problem, so we need to use that.
        // We can't traverse backawrds in a linked list, so instead
        // two pointers at different speeds are needed
        // Important is to find the middle and then check symmetry 'outward'.
        // But can't move outward, so somehow keep track of the left half
        // Let's do double speed for first pointer and when at the
        // end second pointer will be in the middle.
        // As we're going we'll be reversing the first half
        // And finally reset the 'ahead' pointer to point at the reversed list
        // Then it's a straightforward check.

        ListNode* p1 = head;
        ListNode* p2 = head;

        ListNode* prev = nullptr;   // added
        ListNode* temp = nullptr;   // added

        int cntr = 0;

        while (p2 != nullptr && p2->next != nullptr) {  // fixed condition
            p2 = p2->next->next;

            temp = p1->next;     // store next
            p1->next = prev;     // reverse link
            prev = p1;           // move prev
            p1 = temp;           // move slow pointer
            cntr++;
        }

        if (p2 != nullptr) {     // odd length, skip middle
            p1 = p1->next;
        }

        // Now reuse pointer 2 to traverse the reversed list and let p1 finish off the list.
        p2 = prev;
        while (p2 != nullptr && p1 != nullptr) {
            if (p2->val != p1->val) {   // fixed member access
                return false;
            }
            p2 = p2->next;
            p1 = p1->next;
        }
        return true;

    }
};
