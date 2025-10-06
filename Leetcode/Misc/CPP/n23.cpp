// https://leetcode.com/problems/best-time-to-buy-and-sell-stock
// Exceedingly easy problem. Need to start doing more difficult ones. Eventually.
// COMPLETE

#include <vector>
#include <limits>
using namespace std;

auto infinite = [](){ return numeric_limits<float>::infinity(); };

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        float min = infinite();
        float max = 0;
        for (int x : prices) {
            if (x < min) {
                min = x;
            }
            else if (x - min > max) {
                max = x - min;
            }
        }
        return static_cast<int>(max);
    }
};
