// https://leetcode.com/problems/plus-one/

// Daily problem
// Complete

// I like these easy puzzles. However, they don't actually teach me anything

#include <vector>

using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int end  = digits.size() - 1;

        digits[end] ++;

        while (digits[end] == 10 && end >= 1) {
            digits[end] = 0;
            digits[end-1]++;
            end--;
        }

        if (digits[0] == 10) {
            digits[0] = 0;
            digits.insert(digits.begin(), 1);
        }

        return digits;

    }
};
