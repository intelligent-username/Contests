// https://leetcode.com/problems/trapping-rain-water/

// Will re-do with actual dynamic programming
// This is just me understanding the problem to see where I can break it down into smaller problems.

// Complete but INEFFICIENTLY.


class Solution {
public:
    int trap(vector<int>& height) {
        // So we have let's say w numbers.
        // Each number is a height
        // If I just read all the heights "horizontally" (scanning left to right), I can see what's storable
        // So I'll make a 2D grid with the heights, marking as 0 by default and 1 when there's a wall

        int w = height.size();
        int h = *max_element(height.begin(), height.end());

        vector<vector<int>> grid(w, vector<int>(h, 0));

        int x;

        for (int i = 0; i < w; i++) {
            x = height[i];
            for (int j = h - 1; j >= h - x; j--) {
                grid[i][j] = 1;
            }
        }

        // So now we have the grid layed out
        // We just read the grid. Once we encounter a 1, we start counting until we encounter the next 1, at which point we add.
        // If we never encounter a 1, we never add.

        int total = 0;
        
        // if prev is 0, unseen, otherwise seen.
        int prev = 0;
        int temp = 0;

        for (int y = 0; y < h; y++) {
            prev = 0;
            temp = 0;

            for (int i = 0; i < w; i++) {
                if (grid[i][y] == 0) {
                    if (prev == 1) {
                        temp++;
                    }
                }
                else {
                    // Then we see a wall
                    total += temp;
                    temp = 0;
                    prev = 1;
                }
            }
        }

        return total;
    }
};
