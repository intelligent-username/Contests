// https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75
#include <string>
using namespace std;

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string mergedString = "";
        int i = 0, j = 0;
        
        while (i < word1.length() || j < word2.length()) {
            if (i < word1.length()) {
                mergedString += word1[i];
                i++;
            }
            if (j < word2.length()) {
                mergedString += word2[j];
                j++;
            }
        }
        
        return mergedString;
    }
};
