// https://leetcode.com/problems/combinations/

// Complete

class Solution {
public:
    vector<vector<int>> combine(int n, int k) {

        // Tbh idk how this works
        
        int i = 0 ;
        vector<vector<int>> result;
        vector<int> p(k, 0);

        while (i >= 0) {
            p[i]++;            
            if (p[i] > n) i--;
            else if (i == k - 1) result.push_back(p);
            else {
                i++;
                p[i] = p[i - 1];
            }
        }
        return result;
    }
};
