// https://leetcode.com/problems/maximum-subarray/

// Easy

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) {
            return nums[0];
        }

        double cmax = -INFINITY;
        double curr = -INFINITY;

        for (int i = 0; i < n; i++) {
            double x = (double)nums[i];
            curr = max(x, curr + x);
            cmax = max(cmax, curr);
        }
        return cmax;
    }
};