// https://leetcode.com/problems/climbing-stairs/submissions
// Use dynamic programmingtto makeit more efficient later


class Solution {
public:
    int climbStairs(int n) {
        // Yo this is just fibo sequence
        if (n == 0) return 1;
        if (n == 1) return 1;
        return climbStairs(n-1) + climbStairs(n-2);
    }
};
