// https://leetcode.com/problems/increasing-triplet-subsequence
// Good puzzle. Takes a bit to think about.

#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int fs = INT_MAX;
        int ss = INT_MAX;

        for (int crnt : nums) {
            if (crnt > ss) {
                // Found fs < ss < crnt with order preserved
                return true;
            } else if (crnt > fs && crnt < ss) {
                // Valid second element candidate
                ss = crnt;
            } else if (crnt < fs) {
                // New smallest element, restart anchor
                fs = crnt;
            }
        }
        return false;
    }
};
