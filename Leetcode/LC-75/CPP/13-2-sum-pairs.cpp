// https://leetcode.com/problems/max-number-of-k-sum-pairs
// Complete
// Since this is supposed to be a two-pointer problem, I might as well solve the two-pointer version of it as well.

#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        
        // First sort the array
        sort(nums.begin(), nums.end());

        // Then perform the operations.

        int p1 = 0;
        int p2 = nums.size() - 1;

        int cnt = 0;

        while (p1 < p2) {
            // So we don't re-access the same elements (saves some operations)
            int t1 = nums[p1]; 
            int t2 = nums[p2];
            int sum = t1 + t2;

            if (sum == k) {
                cnt++;
                p2--;
                p1++;
            }
            else if (sum < k) {
                // Too low, so we need to up the HIGH END
                p1++;
            }
            else {
                p2--;
            }
        }
        return cnt;
    }
};

