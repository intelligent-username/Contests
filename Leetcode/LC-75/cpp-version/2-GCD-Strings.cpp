// https://leetcode.com/problems/greatest-common-divisor-of-strings/submissions/1205371531/?envType=study-plan-v2&envId=leetcode-75
// COMPLETE

#include <string>

class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        if (str1 + str2 != str2 + str1) {
            return "";
        }
        
        int len1 = str1.length();
        int len2 = str2.length();
        
        int gcd_length = gcd(len1, len2);
        
        return str1.substr(0, gcd_length);
    }
    
private:
    int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
};
