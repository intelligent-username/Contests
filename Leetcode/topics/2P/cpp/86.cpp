// https://leetcode.com/problems/partition-list
// Complete
// Acutally simpler than it seems


using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
    };

 class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        
        ListNode* lower = new ListNode(0);
        ListNode* higher = new ListNode(0);

        auto t1 = lower;
        auto t2 = higher;

        while (head != nullptr) {
            auto temp = head->val;
            if (temp < x) {
                t1->next = head;
                t1 = t1->next;
            }
            else {
                t2->next = head;
                t2 = t2->next;
            }
            head = head->next;
        }
        t2->next = nullptr;
        t1->next = higher->next;
        lower = lower->next;
        return lower;
    }
};
