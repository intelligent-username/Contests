// https://leetcode.com/problems/container-with-most-water
// COMPLETE
// Finally starting to understand two pointer problems
// C++ intution is building
// Life is good

class Solution {
public:
    int maxArea(vector<int>& height) {
        int p1 = 0;
        int p2 = height.size() - 1;

        int max = 0;
        // This is the area.
        // Whichever end is 'shorter', only that one needs to be moved inwards.
        // With this, we'll record all areas efficiently (just once) to 'maximize'.
        // Only record the new highest area, that way you can be accurate
        // Should take about O(n).

        while (p1  < p2) {
            int area = (p2 - p1) * min(height[p1], height[p2]); // Since the lower one determines the total height
            if (area > max) {
                max = area;
            }
            if (height[p1] < height[p2]) {
                p1++;
            }
            else {
                p2--;
            }
        }
        return max;
    }
};
