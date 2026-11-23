// https://leetcode.com/problems/jump-game-ii/description/?envType=problem-list-v2&envId=dynamic-programming

// Complete

class Solution {
public:
    int jump(vector<int>& nums) {
        int end = 0, furthest = 0, cnt = 0;

        int n = nums.size();

        for (int i = 0; i < n-1; i++) {
            furthest = max(furthest, i + nums[i]);
            if (i == end) {
                cnt++;
                end = furthest;
            }
        }
        return cnt;
    }
};
