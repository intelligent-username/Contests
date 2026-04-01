// https://leetcode.com/problems/longest-common-prefix/

// Complete


class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        // I think I have to use a trie
        // But I don't care enough to write one out.
        // And C++ has a built-in sort function

        // Strings are sorted lexographically (that means, in alphabetical order first and be length second)
        // So if we just sort these strings, then we're good to compare first to last
        // Since that's guaranteed to give the longest POSSIBLE prefix across all
        string common = "";

        if (strs.empty()) return common;

        sort(strs.begin(), strs.end());

        const string p1 = strs.front();
        const string p2 = strs.back();

        const int n = p1.size();   

        for (int i = 0; i < n; i++) {
            if (p1[i] != p2[i]) break;
            common += p1[i];
        }
        return common;
    }
};

