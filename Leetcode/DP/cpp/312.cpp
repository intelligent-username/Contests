// https://leetcode.com/problems/burst-balloons/

// Was in the 'dynamic programming' playlist but I didn't really use dynamic programming.
// I know the DFS stack frames are slowing down my solution.
// In the future, I need to rewrite this so it's using actual dynamic programming.

// Complete

class Solution {
public:
    int maxCoins(vector<int>& nums) {
        // This problem looks really hard
        // I don't have a single idea
        // The solution is unique to this problem. It's DP but without a standard template

        // If the sub-problem is 'maximum maxCoins of the remaining two arrays'
        // (after removing a particular one first), we'll have 2^n sub-problems
        // Also, in reality they're connected


        // So we do create a different sub-problem: maximum value IF we pop a given ballon
        // LAST
        // And this way we can still keep the connectedness since it'll be 'last' (on the border, similar to the 1).
        // So it looks like DFS + DP

        // final formula: nums[L-1] * nums[i] * nums[R+1] + cache([i+1][r]) + cache([L][i-1])

        nums.insert(nums.begin(), 1);
        nums.insert(nums.end(), 1);

        // Was using a dictionary but reached a time limit ((
        // 1 <= n <= 300, and 1 on each side for padding, so 302
        
        vector<vector<int>> cache(302, vector<int>(302, -1));

        // dfs lambda function
        function<int(int,int)> dfs = [&](int l, int r) {
            // Can access cache btw

            // Base case: len == 1 or 0
            if (l > r) return 0;

            
            // Or if cached already
            if (cache[l][r] != -1) return cache[l][r];

            // OTHERWISE, CALCULATE
            cache[l][r] = 0;

            for (int i = l; i < r + 1; i++) {
                // Again, tihs is the formula from earlier
                int coins = nums[l - 1] * nums[i] * nums[r + 1];
                coins += dfs(l, i - 1) + dfs(i + 1, r);
                cache[l][r] = max(cache[l][r], coins);
            }

            return cache[l][r];
        };

        int n = nums.size();
        return dfs(1, n - 2);
    }
};
