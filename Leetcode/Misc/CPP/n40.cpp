// https://leetcode.com/problems/integer-to-roman/

// Complete

#include <unordered_map>
#include <string>

using namespace std;

class Solution {
public:
    string intToRoman(int num) {
        unordered_map<string, int> digs = {
            {"I", 1}, {"IV", 4}, {"V", 5}, {"VI", 6}, {"VII", 7},
            {"VIII", 8}, {"IX", 9}, {"X", 10}, {"XL", 40}, {"L", 50},
            {"XC", 90}, {"C", 100}, {"CD", 400}, {"D", 500}, {"CM", 900},
            {"M", 1000}
        };
        
        unordered_map<int, string> order = {
            {0, "M"}, {1, "CM"}, {2, "D"}, {3, "CD"}, {4, "C"}, {5, "XC"},
            {6, "L"}, {7, "XL"}, {8, "X"}, {9, "IX"}, {10, "VIII"}, 
            {11, "VII"}, {12, "VI"}, {13, "V"}, {14, "IV"}, {15, "I"}
        };

        string ans;

        for (int i = 0; i < 16; i++) {
            int curr = digs[order[i]];
            while (num >= curr) {
                ans += order[i];
                num -= curr;
            }
        }

        return ans;
    }
};
