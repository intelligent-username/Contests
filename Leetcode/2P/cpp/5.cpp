// https://leetcode.com/problems/longest-palindromic-substring
// Complete
// Longest Palindromic Substring

#include <string>

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        // This problem seems really complex
        // Don't think I can use the static two pointer methods (alternate speeds or building inwards)
        // Palindrome: when read leftward and rightward, it's the same word.
        // Thinking recursively: 'base case', every character is a palindrome of length 1.
        // Anything that doesn't have length one, needs its left and right sides checked. 
             //If they are identical, then that's also a palindrome
        // But what if the word has an even number of letters? Can't check left and right right away. 
            // But in this case, the left/right would have to have the same letter as the character they're surroudning.
            // Call this character just 'centre' for now.
            // Then, once we pick a centre, we must adjust it to include all characters to its left OR right
            // Until we contian all the ones that are the same as 'it'
        // OK I get it now.

        int p1 = 0;     // Start
        int p2 = 0;     // End
        int maxLen = 0;
        int len = s.size();

        for (int c = 0; c < len; c++) {
            int left = c, right = c;

            // Expand rightward for duplicates
            while (right + 1 < len && s[right+1] == s[right]) {
                right++;
            }

            // Expand symmetrically now
            while (left > 0 && right + 1 < len && s[left-1] == s[right+1]) {
                left--;
                right++;
            }

            int currLen = right - left + 1;
            if (currLen > maxLen) {
                maxLen = currLen;
                p1 = left;
                p2 = right;
            }
        }
        return s.substr(p1, p2 - p1 + 1);
    }
};
