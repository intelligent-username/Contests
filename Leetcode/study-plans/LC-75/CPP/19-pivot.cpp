// https://leetcode.com/problems/find-pivot-index

// Pivot index finding
// Bit interesting
// Hardest part was figuring out the comparison (line 42 - 47), maybe drill that

// Complete

#include <vector>

using namespace std;

class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        // We need the point at which the sum
        // of the array to its LEFT is equal to
        // the sum of the array to it's right
        // Since this is under prefeix sum of LC-75
        // We need a prefix sum :)

        // Oh just build two prefix sum arrays
        // And then see where they're symmetrical.
        // Basically, since we build it "leftward" and
        // "rightward", it's symmetrical when same same
        // index and same value :)

        // If not return -1.
        // Light :)

        int len = nums.size();

        vector<int> left(len + 1, 0);
        vector<int> right(len + 1, 0);

        for (int i = 0; i < len; ++i) {
            left[i+1] = left[i] + nums[i];
        }

        for (int i = 1; i <= len; ++i) {
            right[i] = right[i - 1] + nums[len - i];
        }

        for (int i = 0; i < len; ++i) {
            if (left[i] == right[len-i-1]) {
                return  i;
            }
        }
        return -1;

    }
};
