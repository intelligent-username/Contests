// https://neetcode.io/problems/is-anagram?list=neetcode150
// Complete

#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        int s1 = s.size();
        int s2 = t.size();

        unordered_map<char, int> m1;
        unordered_map<char, int> m2;

        if (s1 != s2) {
            return false;
        }

        for (int i = 0; i < s1; i++) {
            char c1 = s[i];
            char c2 = t[i];            
            
            m1[c1]++;
            m2[c2]++;
        }

        for (auto &[key, value]: m1) {
            if (m2[key] != value) {
                return false;
            }
        }
        return true;
    }
};
