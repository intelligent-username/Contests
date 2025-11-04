// https://leetcode.com/problems/keyboard-row

// Complete

// I wish I had more time to work on this stuff

#include <string>
#include <vector>

using namespace std;



class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        // Make the letter rows
        string row1 = "qwertyuiop", row2 = "asdfghjkl", row3 = "zxcvbnm";

        // Map them to a simple number for simplicity
        vector<int> maps(26);

        for (char c : row1) maps[c - 'a'] = 1;
        for (char c : row2) maps[c - 'a'] = 2;
        for (char c : row3) maps[c - 'a'] = 3;

        vector<string> ans;

        for (string word: words) {
            int row = 0;

            bool add = true;

            for (char c : word) {
                char c2 = tolower(c);
                int arg = maps[c2 - 'a'];

                if (row == 0) {
                    row = arg;
                }
                else if (arg != row) {
                    add = false;
                    break;
                }
            }

            if (add) {
                ans.push_back(word);
            }
        }
        return ans;
    }
};
