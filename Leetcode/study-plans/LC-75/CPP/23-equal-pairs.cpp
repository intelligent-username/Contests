// https://leetcode.com/problems/equal-row-and-column-pairs

// Check for equal row and column pairs
// Complete

#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        int n = grid.size();
        int cnt = 0;
        map<vector<int>, int> rows;
        
        // Build seen rows

        for (vector<int>&v: grid) {
            rows[v]++;
        }

        // Go through the columns to see which ones are equal to seen rows.

        for (int j = 0; j < n; ++j) {
            vector<int> col;
            for (int i = 0; i < n; ++i) {
                col.push_back(grid[i][j]);
            }
            if (rows.count(col)) {
                cnt += rows[col];
            }
        }
        return cnt;


        
    }
};