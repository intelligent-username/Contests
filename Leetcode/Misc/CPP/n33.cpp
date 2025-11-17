// https://leetcode.com/problems/longest-substring-without-repeating-characters/
// Sliding Window Problem (move to 2 Pointers folder?)

// Complete

#include <String>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // Ok I need a sliding window approach

        int b = 0, e = 0;
        int longest = 0;
        unordered_map<char, int> seen;

        int len = s.size();

        while (e < len) {
            char c = s[e];
            if (seen.find(c) != seen.end() && seen[c] > 0) {
                // move start forward until duplicate removed
                while (seen[c] > 0) {
                    seen[s[b]]--;
                    b++;
                }
            }
            seen[c]++;

            int temp = e - b + 1;
            if (temp > longest){
                longest = temp;
            }

            e++;

        }

        return longest;
    }
};
