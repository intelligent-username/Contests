// https://leetcode.com/problems/minimum-path-sum/submissions/

// Complete

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        // Aight, so the minimum path to any given cell is
        // The minimum of min(left, on top)

        int m = grid.size();
        int n = grid[0].size();

        vector<vector<int>> ans(m, vector <int>(n, 0));

                ans[0][0] = grid[0][0];

        // first row
        for (int y = 1; y < n; y++) {
            ans[0][y] = ans[0][y-1] + grid[0][y];
        }

        // first column
        for (int x = 1; x < m; x++) {
            ans[x][0] = ans[x-1][0] + grid[x][0];
        }

        // rest of grid
        for (int x = 1; x < m; x++) {
            for (int y = 1; y < n; y++) {
                ans[x][y] = grid[x][y] + min(ans[x-1][y], ans[x][y-1]);
            }
        }

        return ans[m-1][n-1];

    }
};
