// https://leetcode.com/problems/find-the-highest-altitude

// Complete

#include <vector>

using namespace std;

class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int highest = 0;
        int curr = 0;
        for (int s: gain) {
            curr += s;
            highest = max(curr, highest);
        }

        return highest;
    }
};
