// https://leetcode.com/problems/string-to-integer-atoi/

// String to integer
// Very annoying to get right
// Also not sure how efficient this is

// Complete

class Solution {
public:
    int myAtoi(string s) {
        // string chars = "abcdefghjklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ."
        
        string digs = "0123456789";

        long long ans = 0;
        
        int len = s.size();
        int i = 0;
        
        int sign = 1;
        
        // First read the whitespace
        while (i < len && s[i] == ' ') i++;

        if (i >= len) return ans;

        // Then read the sign
        if (s[i] == '-') {
            sign *= -1;
            i++;
        }
        else if (s[i] == '+') i++;
        
        // Then skip the leading zeroes (don't matter after the sign)

        while (i < len && s[i] == '0') i++;

        if (i >= len) return ans;
        

        // Then read the actual numbers
        while (i < len) {
            char c = s[i];
            if (digs.find(c) != string::npos) {
                ans *= 10;
                ans += (c - '0');
            if (ans * sign > INT_MAX) {
                return INT_MAX;
            }
            else if (ans * sign < INT_MIN) {
                return INT_MIN;
            }

            } else {
                return ans * sign;
            }

            i++;

        }
        ans *= sign;
        return ans;
    }
};
