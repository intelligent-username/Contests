// https://neetcode.io/problems/two-integer-sum?list=neetcode150
// Complete

// Two sum this time actually using a data structure (hash map)
// Note that we know only one answer is there (no sorting, etc. etc.)
// So the first time we see we can just return right away.

#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;

        // Map a number to its lowest index in the array

        int len = nums.size();

        for (int i = 0; i < len; i++) {

            int curr = nums[i];

            // See if the number we need has been seen yet
            auto ex = seen.find(target - curr);

            if (ex != seen.end()) {
                // If it has, then it must've came before i
                return vector<int>{ex->second, i};
            }
            else if (seen.find(curr) == seen.end()) {
                // If it hasn't been seen at all, add it rn
                    // I know it won't be seen more than once via assumption
                    // But this just helps generalize slightly better 
                seen[curr] = i; 

                // Otherwise if it has been seen, no need to add it b/c we need te earliest
            }
        }

        return vector<int>{-1, -1};

    }
};

