// https://leetcode.com/problems/path-sum-ii/

// Complete

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 * int val;
 * TreeNode *left;
 * TreeNode *right;
 * TreeNode() : val(0), left(nullptr), right(nullptr) {}
 * TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 * TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        // Literally just DFS and return if you reach a leaf and have sum == targetSum
        if (!root) return {};
        if (root->left == nullptr && root->right == nullptr) {
            if (root->val == targetSum) return {{root->val}};
            else return {};
        }

        vector<vector<int>> ans;
        vector<int> curr;

        DFS(root, targetSum, ans, curr);

        return ans;

    }
private:
    void DFS(TreeNode* root, int r, vector<vector<int>>& ans, vector<int>& curr) {
        if (!root) return;
        curr.push_back(root->val);

        int val = root->val;

        // If we're at a leaf
        if (!root->left && !root->right && r == val) ans.push_back(curr);
        else {
            DFS(root->left, r - val, ans, curr);
            DFS(root->right, r - val, ans, curr);
        }

        curr.pop_back();

    }
};
