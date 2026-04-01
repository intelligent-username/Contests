// https://leetcode.com/problems/set-matrix-zeroes/

// Complete

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        // Just scan through it and keep track of the coordinates of all the spotted zeroes.
        // Keep the coordinates as a set
        // Then once done iterating, just iterate again and set all to zero

        // IDK why this question is marked as medium but hey free problem

        unordered_set<int> rows;
        unordered_set<int> cols;

        int m = matrix.size();
        int n = matrix[0].size();

        int i;
        int j;

        for (i = 0; i < m; i ++) {
            for (j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    rows.insert(i);
                    cols.insert(j);
                }
            }
        }

        for (int x: rows) {
            for (j = 0; j < n; j++) {
                matrix[x][j] = 0;
            }
        }
        for (int j: cols) {
            for (i = 0; i < m; i ++) {
                matrix[i][j] = 0;
            }
        }
    }
};
