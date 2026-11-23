// https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

// Complete

class Solution {
public:
    long long maximumValueSum(vector<int>& nums, int k, vector<vector<int>>& edges) {
        long long total_sum = 0;
        vector<long long> gains;

        for (int num : nums) {
            total_sum += num;
            gains.push_back((long long)(num ^ k) - num);
        }

        // Sort gains in descending order to pick the best pairs
        sort(gains.rbegin(), gains.rend());

        long long max_extra_gain = 0;
        long long current_pair_gain = 0;

        // Greedy approach: Process nodes in pairs
        for (int i = 0; i + 1 < gains.size(); i += 2) {
            current_pair_gain += (gains[i] + gains[i + 1]);
            // If the sum of this pair increases the total, update max_extra_gain
            if (current_pair_gain > max_extra_gain) {
                max_extra_gain = current_pair_gain;
            }
        }

        return total_sum + max_extra_gain;
    }
};