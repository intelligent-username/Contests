// https://leetcode.com/problems/palindrome-number/
// NOTE: ON LEETCODE, SOME INPUTS ARE INTEGERS BIGGER THAN 2^31

// Complete

#include <stdio.h>

class Solution {
public:
    bool isPalindrome(long x) {
        if (x < 0) {
            return 0;
        }
        // We know it's a positive number now
        // Use modulo arithmetic since strings are a headache (not to mention less efficient) in C++

        long rev = 0;
        long x2 = x;

        while (x2 > 0) {
            rev = rev * 10 + x2 % 10;
            x2 /= 10; 
        }
        return x == rev;

    }
};

int main(void) {
    Solution sol;
    int test1 = 121;
    int test2 = 300;
    int test3 = 293108;

    printf("Test num: %d\n", test1);
    printf("Result: %s\n", sol.isPalindrome(test1) ? "True" : "False");

    printf("Test num: %d\n", test2);
    printf("Result: %s\n", sol.isPalindrome(test2) ? "True" : "False");

    printf("Test num: %d\n", test3);
    printf("Result: %s\n", sol.isPalindrome(test3) ? "True" : "False");

    return 0;
}
