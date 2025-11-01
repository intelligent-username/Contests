
// https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/?
// Easy but was a daily

// Complete

#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    vector<int> getSneakyNumbers(vector<int>& nums) {
        map<int, int> seens;
        vector<int> ret;

        for (int n : nums) {
            if (seens[n] > 0) {
                ret.push_back(n);
                if (ret.size() == 2) {
                    return ret;
                }
            }
            seens[n]++;
        }

        return ret;
    }
};
