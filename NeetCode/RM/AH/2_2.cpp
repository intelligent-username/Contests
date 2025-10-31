// https://neetcode.io/problems/is-anagram?list=neetcode150
// Complete

// Clever trick to slightly improving the solution to  #2
// Slightly faster by only using one hash map
// Only difference is it saves allocation time & metadata by only using one hashmap
// All other constants are basically the same

#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        int s1 = s.size();
        int s2 = t.size();

        unordered_map<char, int> m;

        if (s1 != s2) {
            return false;
        }

        for (int i = 0; i < s1; i++) {
            m[ s[i] ]++;
            m[ t[i] ]--;
        }

        for (auto &[key, value]: m) {
            if (value != 0) {return false;};
        }
        return true;
    }
};
