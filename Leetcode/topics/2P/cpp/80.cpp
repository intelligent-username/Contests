// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

// Complete

#include <vector>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // We know the array is sorted in non-decreasing order
        // So the only time where we have more than a duplicate is when items that are two elements apart are equal. 
        // In that case, 

        int len = nums.size();

        if (len <= 2) {return len;}

        int k = 2; // "head" of the list (actual length)

        for (int i = k; i < len; i++) {
            // Bit unintuitive but got it
            if (nums[i] != nums[k-2]) {
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }
};
