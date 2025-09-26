// https://leetcode.com/problems/linked-list-cycle/
// Another 'easy' difficulty problem with an inefficient solution but I don't have time to spend!!!
// COMPLETE

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

#include <set>
using namespace std;

class Solution {
public:
    bool hasCycle(ListNode *head) {
        set<ListNode*> seen;
        while (head != nullptr) {
            if (seen.count(head)) {
                return true;
            }
            seen.insert(head);
            head = head->next;
        }
        return false;
    }
};

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
