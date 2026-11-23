// https://leetcode.com/problems/max-consecutive-ones-iii

// Complete

#include <vector>

using namespace std;

class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int len = nums.size();

        int top = 0;

        int p1 = 0;
        int p2 = 0;

        
        // This is a dynamic sliding window
        while (p2 < len) {
            if (nums[p2] == 0) {
                k--;
            }

            while (k < 0) {
                if (nums[p1] == 0) {
                    k++;
                }
                p1++;
            }
            top = max(p2 - p1 + 1, top);
            p2++;
        }

        return top;
    }
};
