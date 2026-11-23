#include <vector>
#include <algorithm>
#include <cmath> // Seems to be part of algorithm anyway

using namespace std;

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        // Just need any
        int closest = nums[0] + nums[1] + nums[2];
        int length = nums.size();

        sort(nums.begin(), nums.end());

        for (int i = 0; i < length; i++) {
            int curr = nums[i];
            int p1 = i + 1;
            int p2 = length - 1;

            while (p1 < p2) {
                int n1 = nums[p1];
                int n2 = nums[p2];

                int current_sum = n1 + n2 + curr;
                if (current_sum == target) {
                    return target;
                }
                // ATP, |current_sum - target| > 0
                else if (abs(current_sum - target) < abs(closest - target)) {
                    closest = current_sum;
                }
                if (current_sum > target) p2--;
                else p1++;
            }
        }
        return closest;
    }
};