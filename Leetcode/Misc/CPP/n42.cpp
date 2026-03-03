// https://leetcode.com/problems/climbing-stairs/description/

// Complete

#include <vector>

using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        // Yo now that I think of it recursively, this is just a Fibonacci sequence
        
        if (n == 0) return 1;
        if (n == 1) return 1;

        // But don't do it recursively that'll run out of time

        vector<int> nums(n+1);
        nums[0] = 1;
        nums[1] = 1;

        int i = 2;
        while (i <= n) {
            nums[i] = nums[i-1] + nums[i-2];
            i++;

        }

        return nums[n];
    }
};
