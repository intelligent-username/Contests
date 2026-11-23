# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

# Complete

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Make an array storing (strength, pos)
        # So pos can be a tiebreaker for strength
        # Then make a min-heap based on strength

        tups = [(sum(mat[x]), x) for x in range(len(mat))]
        heapify(tups)

        ans = []
        for j in range(k):
            ans.append(heappop(tups)[1])
        

        return ans
