// https://leetcode.com/problems/interleaving-string/

// Complete

class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int n1 = s1.size();
        int n2 = s2.size();
        int n3 = s3.size();

        if (n1 + n2 != n3) return false;

        vector<vector<int>> dp(n1 + 1, vector<int>(n2 + 1, 0));
        dp[0][0] = 1;

        for (int i = 0; i <= n1; i++) {
            for (int j = 0; j <= n2; j++) {
                int x = i + j;
                if (!dp[i][j]) continue;

                if (i < n1 && s1[i] == s3[x]) dp[i + 1][j] = 1;
                if (j < n2 && s2[j] == s3[x]) dp[i][j + 1] = 1;
            }
        }

        return dp[n1][n2];
    }
};