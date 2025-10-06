// https://leetcode.com/problems/max-number-of-k-sum-pairs
// COMPLETE

#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        // For this to be a two pointer problem, the list needs to already be sorted. 
        // Sorting would take too long. 
        // I'll just solve using a simpler method

        // Keep track of which integers are availalble
        unordered_map<int, int> seen; 
        int cnt = 0;
        
        for (int n: nums) {
            // Note: if (k - n) == 0, we have a valid pair. (In this case let n be the pair) 
            // Otherwise, throw it into storage.
            if (seen[k - n] >= 1){
                seen[k-n]--;
                cnt++;
            }
            else {
                seen[n] ++;
            }
        }
        return cnt;
    }
};
