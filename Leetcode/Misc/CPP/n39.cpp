// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree


// CPP Version just

// Complete

#include <vector>;
#include <Cmath>;

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
    int maxLevelSum(TreeNode* root) {
        int maxSum = INT_MIN;
        int maxLoc = 0;

        int index = 0;

        vector<TreeNode*> curr = {root};
        vector<TreeNode*> next;

        while (!curr.empty()) {
            int temp = 0;
            index++;
            for (TreeNode* t: curr) {
                if (t != nullptr) {
                    temp += t->val;
                    if (t->left != nullptr) {
                        next.push_back(t->left);
                    }
                    if (t->right != nullptr) {
                        next.push_back(t->right);
                    }
                }
            }
            if (temp > maxSum) {
                maxSum = temp;
                maxLoc = index;
            }

            curr = next;
            next.clear();

        }

        return maxLoc;

    }
};
