// https://leetcode.com/problems/divide-two-integers

// Complete

#include <climits>
#include <cstdlib>

using namespace std;

class Solution {
public:
    int divide(int dividend, int divisor) {
        // First handle the overflow case (only 32-bit can be handled as given)

        if (dividend == INT_MIN && divisor == -1) {
            return INT_MAX;
        }

        int sign = ((dividend < 0) ^ (divisor < 0)) ? -1 : 1;

        long long dividend2 = llabs((long long) dividend);
        long long divisor2 = llabs((long long) divisor);

        long long quotient = 0;

        // THANKS TO CSC258, I know about left shift
        // And C++ has a left shift operator :)

        while (dividend2 >= divisor2) {
            long long tmp = divisor2;
            long long mult = 1;

            // (Find power of 2)

            while ((tmp << 1) <= dividend2) {  // Fixed: should compare with dividend2, not divisor2
                tmp <<= 1;
                mult <<= 1; 
            }

            dividend2 -= tmp;
            quotient += mult;  // Fixed: should add mult, not subtract
        }

        quotient *= sign;

        return int(quotient);
    }
};
