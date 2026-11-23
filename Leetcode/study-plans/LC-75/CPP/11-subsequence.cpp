// https://leetcode.com/problems/is-subsequence
// Was fun idk

#include <string>
using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        // Check if s is in t
        // eeeeeeeez

        int char1 = 0;
        int chars = 0;

        while (char1 < s.size() && chars < t.size()) {
            if (s[char1] == t[chars]) {
                char1++;
            }
            chars++;
        }
        return char1 == s.size();
    }
};