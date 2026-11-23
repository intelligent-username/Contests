// https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element

// Complete

#include <vector>
#include <Cmath>

using namespace std;


class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int z = 0; // Num of zeroes
        int p1 = 0;
        int len = nums.size();
        int biggest = 0;

        // Read through the whole array
        // Keep track of the longest sequence possible 
        // for all z <= 1
        for (int p2 = 0; p2 < len; p2++) {
            if (nums[p2] == 0){
                z++;
            }

            while (z > 1) {
                if (nums[p1] == 0) {
                    z--;
                }
                p1++;
            }

            biggest = max(biggest, p2 - p1);
            // Note that p2 - p1 automatically "deletes one element"
            // Since p1 starts at 0

        }

        return biggest;
    }
};
