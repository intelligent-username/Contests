// https://leetcode.com/problems/roman-to-integer/
// Roman Numeral to integer converter

#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        // Constraints:

        // 1 <= s.length <= 15
        // s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
        // It is guaranteed that s is a valid roman numeral in the range [1, 3999].

        unordered_map<char, int> charVals;
        // I can be placed before V (5) and X (10) to make 4 and 9. 
        // X can be placed before L (50) and C (100) to make 40 and 90. 
        // C can be placed before D (500) and M (1000) to make 400 and 900.

        charVals['M'] = 1000;
        charVals['D'] = 500;
        charVals['C'] = 100;
        charVals['L'] = 50;
        charVals['X'] = 10;
        charVals['V'] = 5;
        charVals['I'] = 1;

        // vector<string> chars = {"M", "D", "C", "L", "X", "V", "I"};

        int sum = 0;

        for (size_t i = 0; i < s.size(); i++) {
            if (i+1 < s.size() && charVals[s[i]] < charVals[s[i+1]]) {
                sum -= charVals[s[i]];
            }
            else {
                sum += charVals[s[i]];
            }
        }
        return sum;
    }
};

int main(void) {
    Solution sol;
    string test1 = "III";       // 3
    string test2 = "LVIII";     // 58
    string test3 = "MCMXCIV";   // 1994

    printf("Test String: %s\n", test1.c_str());
    printf("Result: %d\n", sol.romanToInt(test1));

    printf("Test String: %s\n", test2.c_str());
    printf("Result: %d\n", sol.romanToInt(test2));

    printf("Test String: %s\n", test3.c_str());
    printf("Result: %d\n", sol.romanToInt(test3));

    return 0;
}
