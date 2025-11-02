// https://leetcode.com/problems/reverse-integer
// Overflow handling very annoying.
// Low key better to just convert to string and check size using string's characters

// COMPLETE

#include <cmath>

class Solution {
public:
    int reverse(int x) {
        int n = 0;
        int pwr = 0;

        while (x != 0) {
            int digit = x % 10;

            if (n > INT_MAX / 10 || (n == INT_MAX / 10 && digit > 7)) {
                return 0;
            }
            if (n < INT_MIN / 10 || (n == INT_MIN / 10 && digit < -8)) {
                return 0;
            }

            n = n * 10 + digit;
            x /= 10;
        }

        return n;
    }
};
