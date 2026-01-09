// https://leetcode.com/problems/find-the-difference-of-two-arrays/

// Find the difference of two arrays
// Really enjoying these easy problems

// Complete

#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        
        // MORE CONCISE declaration method detected!!
        unordered_set<int> s1(nums1.begin(), nums1.end());
        unordered_set<int> s2(nums2.begin(), nums2.end());
        // Still O(n) but saves space

        vector<int> r1;
        vector<int> r2;

        // WAS ITERATING OVER THE ORIGINAL LIST
        // BUT I CAN SAVE TIME BY ITERATING OVER THE SET!!

        for (int s: s1) {
            if (s2.find(s) == s2.end()) {
                r1.push_back(s);
            }
        }

        for (int s: s2) {
            if (s1.find(s) == s1.end()) {
                r2.push_back(s);
            }
        }

        return {r1, r2};

    }
};
