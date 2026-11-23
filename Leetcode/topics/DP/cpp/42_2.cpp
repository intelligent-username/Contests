// https://leetcode.com/problems/trapping-rain-water/

// Re-did it properly :)

// Completed

class Solution {
    public:
        int trap(vector<int>& height) {
            // Ok, adding on to before, instead of scanning every row, which'll be O(n^2) due to the grid
            // Scan every INDEX

            int total = 0;
            int n = height.size();

            // Re-thinking the previous solution, we say

            // The maximum water that can be stored at any given point (or HEIGHT) is limited by the max height on it's left and on it's right

            // So left's max = max(heights 0:i)
            // And right's max = max(heights i : n - 1)

            vector<int> left(n);
            vector<int> right(n);

            left[0] = height[0];

            for (int i = 1; i < n; i ++) {
                left[i] = max(left[i-1], height[i]);
            }

            right[n-1] = height[n-1];
            for (int i = n - 2; i >= 0; i--) {
                right[i] = max(right[i + 1], height[i]);
            }

            for (int i = 0; i < n; i++) {
                total += min(left[i], right[i]) - height[i];
            }

            return total;
        }
    };