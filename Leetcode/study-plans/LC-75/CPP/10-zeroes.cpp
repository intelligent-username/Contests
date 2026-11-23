

#include <vector>
#include <algorithm>

class Solution {
public:
    void moveZeroes(std::vector<int>& nums) {
        int ogsize = nums.size();

        // Get rid of zeroes while preserving structure
        nums.erase(remove(nums.begin(), nums.end(), 0), nums.end());

        // Figure out how many zeroes to append to the end of the list.
        int app = ogsize - nums.size();
        while (app > 0) {
            nums.push_back(0);
            app--;
        }
    }
};