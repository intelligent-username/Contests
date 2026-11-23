// https://leetcode.com/problems/counting-bits/

// Complete

class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> nums(n+1, 0);

        // Writing all numbers from 0 to n
        // At each 0<=[i]<=n in nums, find write how many 1s appear
        // In the binary version of i

        // I think 
        // Hm
        // Ok so the number's binary representation is identical + a one in the lead if it's a power of two apart
        // That's the pattern I see
        // So we can DP on that
        // But this is only if perfect powers of 2
        // If not a perfect power of 2, then we need the difference between i and i // 2
        // Oh
        for (int i = 1; i < n + 1; i++) {
            nums[i] = nums[i >> 1] + (i & 1);
        }

        return nums;



    }
};
