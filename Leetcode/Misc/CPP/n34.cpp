// https://leetcode.com/problems/keep-multiplying-found-values-by-two/?envType=daily-question&envId=2025-11-19
// Crazy easy daily problem
// Complete

// More clever would be to do some smart iteration (like itereate from 0 to size, then every time found, reset the iterator to 0, and repeat until we don't find)

#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    int findFinalValue(vector<int>& nums, int original) {
        unordered_set<int> s;

        for (int n: nums) {
            s.insert(n);
        }

        while (s.find(original) != s.end()) {
            original *= 2;
        }

        return original;

    }
};
