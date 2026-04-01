// https://leetcode.com/problems/generate-parentheses/

// Complete

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        // All possible combinations of ( + ) pairs

        // Every ) needs to be preceeded by a (
        // So ) can't be first
        // And ( can't be last

        vector<string> pars;

        gen(pars, "", 0, 0, n);
        return pars;
    }

private:
    void gen(vector<string>& ls, string str, int l, int r, int n) {
        // 'l' is left debt
        // 'r' is how many we have still
        if (str.size() == n * 2) {
            ls.push_back(str);
            return;
        }

        if (l < n) {
            gen(ls, str + '(', l + 1, r, n);
        }
        if (r < l) {
            gen(ls, str + ')', l, r + 1, n);
        } 
    }
};
