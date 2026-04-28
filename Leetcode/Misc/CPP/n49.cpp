// https://leetcode.com/problems/ransom-note/ 

// Complete

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int a[26] = {0};
        for (char c: magazine) {
            a[c - 'a']++;
        }

        for (char c: ransomNote) {
            if (--a[c - 'a'] < 0) return false;
        }
        return true;
    }
};