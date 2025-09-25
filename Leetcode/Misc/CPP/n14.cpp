// https://leetcode.com/problems/two-sum/
// Two sum: literally one of the easiest problems ever but I'm trying to get my reps in for the day and don't have the time to do a proper problem

#include <vector>
#include <set>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        set<pair<int,int>> combos;
        int length = nums.size();
        
        for (int i = 0; i < length; i++) {
            for (int j = i + 1; j < length; j++) {  // avoid self-pairing and duplicates
                if (nums[i] + nums[j] == target) {
                    combos.insert({i, j});
                }
            }
        }

        // Return the first valid pair as a vector<int>
        if (!combos.empty()) {
            auto first_pair = *combos.begin();
            return {first_pair.first, first_pair.second};
        }

        return {};  // return empty vector if no solution
    }
};
