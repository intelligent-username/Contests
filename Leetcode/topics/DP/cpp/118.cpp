// https://leetcode.com/problems/pascals-triangle

// Completed LeetCode/DP/cpp;  code 97.cpp

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> rows(numRows);
        rows[0] = {1};
        if (numRows == 1) {
            rows[0] = {1};
            return rows;
        }
        rows[1] = {1, 1};

        int i;
        int j;
        for (i = 2; i < numRows; i++) {
            rows[i].resize(i + 1);
            rows[i][0] = 1;
            for (j = 1; j < i; j++) {
                rows[i][j] = rows[i-1][j] + rows[i-1][j-1];
            }
            rows[i][j] = 1;
        }

        return rows;
    }
};
