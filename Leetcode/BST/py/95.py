# https://leetcode.com/problems/unique-binary-search-trees-ii/

# Actually happened to think of the same solution as the editorial it looks like.

# Complete

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        if n  == 1:
            return [TreeNode(1)]
        
        def subgen(low, i, top) -> Tuple(List[Optional[TreeNode]], List(Optional[TreeNode])):
            """
            Return all possible set of left children and all possible lists of right children

            low: the low end
            i: the 'middle'
            top: the top end
            """
            
            # Left children are the numbers from low to i
            # Right children are numbers from i to max
            
            # Need every possible tree with each

            lefts = []
            rights = []

            if low > i - 1:
                lefts.append(None)
            else:
                for j in range(low, i):
                    lft, rgt = subgen(low, j, i-1)
                    for x in lft:
                        for y in rgt:
                            node = TreeNode(j)
                            node.left = x
                            node.right = y
                            lefts.append(node)

            if top < i + 1:
                rights.append(None)
            else:
                for j in range(i + 1, top + 1):
                    lft, rgt = subgen(i + 1, j, top)
                    for x in lft:
                        for y in rgt:
                            node = TreeNode(j)
                            node.left = x
                            node.right = y
                            rights.append(node)

            return (lefts, rights)

        # I need every single unique way of conuting from 1 to n using BSTs
        # So obviously I need to recurse

        # Ok for every i from 1 to n
        # Make *it* the root
        # Then generate all possible arrangements of children it could have
        # And we recurse this way with all the children of i itself

        ans = []

        for i in range(1, n+1):
            # Left is every single possible left child
            # Right is every single possible right child
            left, right = subgen(1, i, n)
            
            # For each possible left child, give it every possible right child.
            for x in left:
                for y in right:
                    s = TreeNode(i)
                    s.left = x
                    s.right = y
                    ans.append(s)

        return ans
    