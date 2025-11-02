// https://leetcode.com/problems/median-of-two-sorted-arrays/

// Median of two sorted arrays.
// Very trippy

// Complete

#include <vector>
#include <climits>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // OK we want the mean of two sorted arrays
        // Both are sorted in non-decreasing order
        // However, we can't just merge them since we need log(m+n) runtime.

        // Still, the median splits the merged array into two equal halves.
        // If I could straight up read through both of them, I would search ahead with two pointers until the sum of their positions was the halfway point of the length of both.
        // This is the right solution. But I can't search like that. 

        // Still, the position of the median, when merged, is >= the position of the median of the longer one

        // Idk what to do from here, let's just find the position of the bigger one first.

        int l1 = nums1.size();
        int l2 = nums2.size();

        // Ensure nums1 is smaller to avoid the headache
        if (l1 > l2) {
            swap(nums1, nums2);
            swap(l1, l2);
        }

        // The searching idea is still correct, I just need a faster version
        // Why not b inary search

        int x = 0;
        int y = l1;

        while (x <= y) {
            int i = (x + y) / 2;                       // partition in smaller array
            int j = ((l1 + l2 + 1) / 2) - i;           // partition in larger array

            int leftA, rightA, leftB, rightB;

            if (i == 0) leftA = INT_MIN; else leftA = nums1[i - 1];
            if (i == l1) rightA = INT_MAX; else rightA = nums1[i];
            if (j == 0) leftB = INT_MIN; else leftB = nums2[j - 1];
            if (j == l2) rightB = INT_MAX; else rightB = nums2[j];

            if (leftA <= rightB && leftB <= rightA) {
                if ((l1 + l2) % 2 == 0)
                    return (double)(std::max(leftA, leftB) + std::min(rightA, rightB)) / 2;
                else
                    return (double)std::max(leftA, leftB);
            } else if (leftA > rightB) {
                y = i - 1;
            } else {
                x = i + 1;
            }
        }

        // If didn't work then idk what happened
        return -1; 

    }
};
