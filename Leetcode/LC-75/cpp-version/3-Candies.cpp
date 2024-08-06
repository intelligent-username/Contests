// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75
// COMPLETE

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> res(candies.size(), false);
        int max_candies = *(max_element(candies.begin(), candies.end()));
        for(int i=0;i<candies.size();i++){
            res[i] = (max_candies <= candies[i] + extraCandies);
        }
        return res;
    }
};