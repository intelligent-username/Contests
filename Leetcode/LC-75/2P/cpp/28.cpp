// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
// Two Pointers
// Complete

#include <string>

using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.empty()) return -1;

        int size = needle.size() - 1;
        int p1 = 0;
        int p2 = size;

        if (needle.size() > haystack.size()) return -1;

        while (p2 < haystack.size()) {
            if (haystack[p1] != needle[0] || haystack[p2] != needle[size]) {
                p1++;
                p2++;
            } else {
                // Reset and go again
                int left = p1;
                int right = p2;
                int t1 = 0;
                int t2 = size;
                bool found = true;

                while (left <= right) {
                    if (haystack[left++] != needle[t1++] || haystack[right--] != needle[t2--]) {
                        found = false;
                        break;
                    }
                }
                if (found) return p1;
                p1++;
                p2++;
            }
        }
        return -1;

    }
};
