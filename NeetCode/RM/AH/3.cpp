// https://neetcode.io/problems/two-integer-sum?list=neetcode150
// Complete

// Two sum ofc
// Brute force version

#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // If we naively check all combinations, that'll take O(n^2)
        // If we sort then use two pointers, that'll take nlog(n)
        // i.e. nlog(n) to sort and n to scan through
        // HOWEVER that would mess up the indices
        int s = nums.size();

        for (int i = 0; i < s; i++) {
            for (int j = i+1; j < s; j++) {
                if (nums[i] + nums[j] == target) {return vector<int>{i, j};};
            }
        }
        // Answer may not exist but by the assumption 
        // (You may assume that every input has exactly one pair
        // of indices i and j that satisfy the condition)
        // We can assume it does
        // So return whatever

        return vector<int>{-1, -1};

    }
};
