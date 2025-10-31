// https://neetcode.io/problems/duplicate-integer?list=neetcode150
// Complete

#include <set>
#include <vector>

using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> seen;

        for (int i : nums) {
            if (seen.count(i)) {
                return true;
                }
            else {
                seen.insert(i);
            }
        }
        return false;

    }
};
