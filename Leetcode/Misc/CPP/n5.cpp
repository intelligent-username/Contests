// https://leetcode.com/problems/length-of-last-word/
// 'Count the length of the last word in the string'
#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        // Return the length of the last word in the string
        int len = 0;
        int i = s.size() - 1;

        // Make sure to skip trailing whitespace so you don't FAIL THE TEST CASES!
        while (i >= 0 && s[i] == ' ') i--;
        
        while (i >= 0  && s[i] != ' '){
                i -= 1;
                len += 1;
            }

        return len;
    }
};

int main() {
    Solution sol;
    
    string tests[] = {
        "Hello World",
        "   fly me   to   the moon  ",
        "singleword",
        "trailing spaces   ",
        "    "
    };

    for (int i = 0; i < 5; i++) {
        cout << "Test String #" << i+1 << ": \"" << tests[i] << "\"\n\t-> Length of last word: "
             << sol.lengthOfLastWord(tests[i]) << "\n";
    }

    return 0;
}


