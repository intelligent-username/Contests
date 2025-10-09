// https://leetcode.com/problems/next-permutation
// Complete


#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int len = nums.size();
        int p1 = len - 2;       // 'Rightmost' side

        // Skip non-increasing suffix
        while (p1 >= 0 && nums[p1] >= nums[p1+1]) { 
            p1--;
        }

        if (p1 < 0) {
            // Then all nums are in descending order
            reverse(nums.begin(), nums.end());
        }
        else {
            int p2 = len - 1;

            // Travel left until you find a number greater than nums[p1]
            while (p2 > p1 && nums[p2] <= nums[p1]) {
                p2--;
            }

            // Swap nums[p1] and nums[p2]
            swap(nums[p1], nums[p2]);

            // Reverse suffix starting at p1+1
            reverse(nums.begin() + p1 + 1, nums.end());
        }
        return;
    }
};
