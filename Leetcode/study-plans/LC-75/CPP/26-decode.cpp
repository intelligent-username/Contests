// https://leetcode.com/problems/decode-string

// Complete

#include <string>
#include <stack>
#include <cctype>

using namespace std;

class Solution {
public:
    string decodeString(string s) {
        // Thinking: read the string from the "inside out"
        // So do the inner repeats first
        // Then outer repeats
        // Hence the stack, the closer in, the more repeas of the currently formed string that we do
        // Need a way to handle multiple separate strings


        // Ok, so iterate forwards, and every time we a sub-stack of strings
        // Map every sub-stack to the number of times it's going be repeated.

        string ans = "";


        // Instead of mapping "stack" or string to count, I'll just build two parallel stacks
        stack<int> counts;
        stack<string> words;

        int currNum = 0;
        string currString = "";

        for (char c : s) {
            if (isdigit(c)) {
                currNum = currNum * 10 + (c - '0');
            }
            else if (c == '[') {
                counts.push(currNum);
                words.push(currString);
                currNum = 0;
                currString.clear();
            }
            else if (c == ']') {
                int repeat = counts.top(); counts.pop();
                string prev = words.top(); words.pop();
                while (repeat--) prev += currString;
                currString = prev;
            }
            else {
                currString += c;
            }
        }

        return currString;
    }
};
