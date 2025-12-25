// https://leetcode.com/problems/apple-redistribution-into-boxes
// Was daily problem

// Simple greedy algo
// Complete

#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minimumBoxes(vector<int>& apple, vector<int>& capacity) {
        int total = 0;
        for (int s: apple) {
            total += s;
        }

        sort(capacity.begin(), capacity.end(), greater<int>());
        
        int used = 0;
        int count = 0;

        for (int c : capacity) {
            used += c;
            count++;
            if (used >= total) {
                return count;
            }
        }

        return count;
    }
};
