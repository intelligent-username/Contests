// https://leetcode.com/problems/search-insert-position/
// Simple Binary Search implementation, good fun
// COMPLETED

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int end = nums.size();
        if (end == 0) {
            return 0;
        }
        int b = 0;
        while (b < end) {
            int mid = (b + end)/2;
            if (nums[mid] == target) {
                return mid;
            }
            else if (nums[mid] > target) {
                end = mid; // Target to the left of middle
            }
            else {
                b = mid + 1; // Target to the right of middle
            }
        }
        return end;
    }
};