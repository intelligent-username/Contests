// https://leetcode.com/problems/determine-if-two-strings-are-close

// Determine if two strings are close

// Complete

#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool closeStrings(string word1, string word2) {
       // I think all this could be simplified to use less data structures, etc.
       // But whatever.
       
        int l1 = word1.size();
       int l2 = word2.size();
       if (l1 != l2) {
            return false;
       }
       unordered_map<char, int> m1;
       unordered_map<char, int> m2;

       for (int i = 0; i < l1; i++) {
            m1[word1[i]]++;
            m2[word2[i]]++;
       }

        unordered_set<char> cs1, cs2;
        vector<int> cc1, cc2;

        for (auto& n: m1) {
            cs1.insert(n.first);
            cc1.push_back(n.second);
        }

        for (auto& n: m2) {
            cs2.insert(n.first);
            cc2.push_back(n.second);
        }

        sort(cc1.begin(), cc1.end());
        sort(cc2.begin(), cc2.end());

        return cs1 == cs2 && cc1 == cc2;

    }
};
