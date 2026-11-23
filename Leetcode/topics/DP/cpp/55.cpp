// https://leetcode.com/problems/jump-game/

// Complete

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        int furthest = 0;
        if (n == 1) return true;
        for (int i = 0; i < n; i++) {
            if (i > furthest) {
                return false;
            } else {
                furthest = max(furthest, i + nums[i]);
            }
            if (furthest >= n-1) return true;
        }
        return false;
    }
};