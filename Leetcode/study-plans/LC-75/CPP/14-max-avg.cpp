// https://leetcode.com/problems/maximum-average-subarray-i/

// Complete

#include <vector>

using namespace std;

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        // Sliding window

        double temp = 0;
        int len = nums.size();
        
        int p1 = 0;
        int p2 = k;

        for (int i = p1; i < k; i++) {
            temp += nums[i];
        }

        double max = temp;

        while (p2 < len) {
            temp -= nums[p1];
            temp += nums[p2];

            if (temp > max) {
                max = temp;
            }
            p1++;
            p2++;
        }

        return max/k;

    }
};
