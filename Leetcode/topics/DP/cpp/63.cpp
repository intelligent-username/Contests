// https://leetcode.com/problems/unique-paths-ii/

// Complete

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();

        if (obstacleGrid[0][0] == 1) return 0;
        if (m == 1 && n == 1) return 1;
        
        vector<vector<int>> ans(m, vector<int>(n, 0));

        // first row
        for (int j = 1; j < n; j++) {
            if (obstacleGrid[0][j] == 1) break;
            ans[0][j] = 1;
        }

        // first column
        for (int i = 1; i < m; i++) {
            if (obstacleGrid[i][0] == 1) break;
            ans[i][0] = 1;
        }

        // Now same logic as prev question

        for (int x = 1; x < m; x++) {
            for (int y = 1; y < n; y++) {
                if (obstacleGrid[x][y] == 1)
                    ans[x][y] = 0;
                else
                    ans[x][y] = ans[x-1][y] + ans[x][y-1];
            }
        }

        return ans[m-1][n-1];

    }
};