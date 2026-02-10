# https://leetcode.com/problems/unique-binary-search-trees

# Complete

class Solution:
    def numTrees(self, n: int) -> int:
        # 0 and 1 have 1
        # 2 has the number of ways of placing the first one times the number of ways of placing the second one.
        # So that's 1 + 1 = 2
        # And so on
        # How many we can make depends on the root (and we can choose whatever roots we want, etc.)
        # And from here we can treat the children as the new roots and run the same math on them

        # So if I pick the i-th smallest number, I'll have i - 1 nodes to the left and n-i nodes to the right.

        # So, we have n possible options for the root. Then, depending on what we choose for the root, we get even more options for the children.

        # Solved this recursively at first but it was growing exponentially in time cmoplexity

        times = {0: 1, 1: 1, 2: 2}

        for i in range(2, n+1):
            total2 = 0

            for j in range(i):
                total2 += times[j] * times[i - j - 1]
            
            times[i] = total2

        return times[n]
