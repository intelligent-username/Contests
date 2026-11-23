// https://leetcode.com/problems/4sum/
// Complete
// Good, need more of these before moving on to other problem types.


#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int len = nums.size();

        vector<vector<int>> answers;

        for (int x = 0; x < len - 3; x++) {
            if (x > 0 && nums[x] == nums[x - 1]) continue;
            for (int y = x + 1; y < len - 2; y++) {
                if (y > x + 1 && nums[y] == nums[y - 1]) continue;

                // Fix first two
                // Then last two (iterate inwards, knowing the list is sorted)
                int i = y + 1;
                int j = len - 1;
                while (i < j) {
                    long long sum = (long long)nums[x] + nums[y] + nums[i] + nums[j];
                    if (sum == target) {
                        answers.push_back({nums[x], nums[y], nums[i], nums[j]});
                        while (i < j && nums[i] == nums[i + 1]) i++;
                        while (i < j && nums[j] == nums[j - 1]) j--;
                        i++;
                        j--;
                    } else if (sum < target) {
                        i++;
                    } else {
                        j--;
                    }
                }
            }
        }

        return answers;

    }
};
