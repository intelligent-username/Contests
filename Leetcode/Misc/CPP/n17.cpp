// https://leetcode.com/problems/sqrtx
// TWO solutions today :O

class Solution {
public:
    int mySqrt(int x) {
        if (x == 0) return 0;
        if (x == 1) return 1;

        long guess = x / 2;
        while (guess * guess > x) {
            guess = (guess + x / guess) / 2;
        }
        if ((guess + 1) * (guess + 1) <= x) return guess + 1;
        return guess;
    }
};
