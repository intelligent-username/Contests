// https://leetcode.com/problems/valid-number/
// Hard Difficulty; I have no idea how to optimize this properly
// COMPLETE

#include <string>
#include <set>

using namespace std;

class Solution {
public:
    bool isNumber(string s) {
        if (s.empty()) return false;
        set<char> digits = {'0','1','2','3','4','5','6','7','8','9'};
        set<char> signs = {'+', '-'};
        set<char> valid_chars = {'.'};
        valid_chars.insert(digits.begin(), digits.end());
        valid_chars.insert(signs.begin(), signs.end());
        // Only valid first chars

        // Store things like e/E, dot ., or a sign 
        if (valid_chars.find(s[0]) == valid_chars.end()) {
            return false;
        }

        // Once we know string is non-empty and starts validly, more characters are available to us
        set<char> exp = {'e', 'E'};
        valid_chars.insert(exp.begin(), exp.end());

        // e or E cannot be first
        bool e_seen = false;
        bool e_followed = true;
        bool sign_seen = false;
        bool dot_seen = false;
        bool num_exists = false;
        bool need_digit_after_exp = false;

        // A sign must not be preceded by anything except e/E.
        // e/E may only appear once
        // 'e' or 'E' must be followed by one sign or some number of digits and immediately terminate 
        // (no decimals or signs)
        // dot (.) can't be preceded by an e/E

        // Main loop
        // I'm going to nest the if conditions because, that's more efficient (don't have to check all else-ifs).
        int len = s.size();
        for (int i = 0; i < len; i++) {
            char c = s[i];
            if (valid_chars.find(c) == valid_chars.end()) {
                return false; // invalid character
            }

            if (digits.find(c) != digits.end()) {
                num_exists = true;
                if (e_seen) {
                    e_followed = true;
                    need_digit_after_exp = false;
                }
            }
            else if (signs.find(c) != signs.end()) {
                if (i == 0 || (i > 0 && exp.find(s[i-1]) != exp.end())) {
                    sign_seen = true; // sign at start or after exponent
                } else {
                    return false;
                }
            }
            else if (c == '.') {
                // Ensure it's the only dot and not in exponent
                if (dot_seen || e_seen) {
                    return false;
                }
                dot_seen = true;
            }
            else if (exp.find(c) != exp.end()) {
                // Ensure exponent rules
                if (e_seen || !num_exists) {
                    return false;
                }
                e_seen = true;
                e_followed = false;
                need_digit_after_exp = true;
            }
        }

        // Must have digits and exponent must be followed by digits
        return num_exists && e_followed && !need_digit_after_exp;
    }
};
