// https://leetcode.com/problems/combination-sum/
// DFS Problem, interesting, need to do more of these

#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> cur;
        dfs(0, target, candidates, cur, res);
        return res;
    }

private:
    void dfs(int i, int remain, vector<int>& candidates, vector<int>& cur, vector<vector<int>>& res) {
        if (remain == 0) {
            res.push_back(cur);
            return;
        }
        if (i >= candidates.size() || remain < 0) return;

        // choose current candidate
        cur.push_back(candidates[i]);
        dfs(i, remain - candidates[i], candidates, cur, res); // reuse same element
        cur.pop_back();

        // skip current candidate
        dfs(i + 1, remain, candidates, cur, res);
    }
};
