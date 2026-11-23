// https://leetcode.com/problems/binary-tree-level-order-traversal

// Complete

#include <vector>

using namespace std;

/**
 * Definition for a binary tree node.
**/

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {

        if (!root) {
            return vector<vector<int>>();
            // Just learnt I can also do return {};
        }

        vector<vector<int>> order;

        vector<TreeNode*> curr = {root};
        vector<TreeNode*> next;

        while (!curr.empty()) {
            vector<int> vals;
            for (auto& x: curr) {

                if (x != nullptr) {
                    vals.push_back(x->val);
                    if (x->left) {
                        next.push_back(x->left);
                    }
                    if (x->right) {
                        next.push_back(x->right);
                    }
                }
            }
            order.push_back(vals);
            curr = next;
            next.clear();

        }

        return order;
        
    }
};
