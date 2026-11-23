// https://leetcode.com/problems/pascals-triangle-ii/description/

// Complete

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        // I know there's a formula for it (n choose k), which I used to know
        // But I don't know it right now
        // So I'm just going to build from scratch
        vector<vector<int>> rows(2);
        rows[0] = {1};
        rows[1] = {1, 1};
        if (rowIndex == 0) {
            return rows[0];
        }
        if (rowIndex == 1) {
            return rows[1];
        }

        // Row i has i + 1 items
        // First, last element is 1
        // Then every i-th element is the sum of the (i-1)th + (i)th elements from the previous row

        int i;
        int j;
        vector<int> back;
        
        for (i = 2; i <= rowIndex; i++) {
            vector<int> currRow(i+1);
            currRow[0] = 1;
            back = rows.back();
            for (j = 1; j < i; j++) {
                currRow[j] = back[j-1] + back[j];
            }
            currRow[i] = 1;
            rows.push_back(currRow);
        }

        return rows.back();
        
    }
};
