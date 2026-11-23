// https://leetcode.com/problems/sort-colors/submissions/1834836444/?envType=problem-list-v2&envId=two-pointers&utm_source=chatgpt.com

// Complete

#include <vector>

using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        // It's not quite asking for generic sorting
        // It wants me to use two pointers
        // Btw red, white, and blue 💪💪

        // This looks simple. Just store where the smallest index of twos is, and the biggest index of 0s.
        // Every time a 0 is seen, move the zeroes index forward and swap with the seen place.
        // Every time a 2 is seen, move the 2s index backwards and swap
        // The ones will end up sorting themselves basically

        int h = nums.size() - 1, l = 0, c = 0;
        // High, low, and current

        while (c <= h) {
            if (nums[c] == 0) {
                swap(nums[c], nums[l]);
                l++;
                c++;
            } else if (nums[c] == 2) {
                swap(nums[c], nums[h]);
                h--;
            } else { // nums[c] == 1
                c++;
            }
        }
    }
};
