# https://leetcode.com/problems/count-square-submatrices-with-all-ones

# Complete

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        l= len(matrix)
        w = len(matrix[0])

        dp = [[0]*w for _ in range(l)]

        total  = 0
        # At each x, y in the matrix, the number of square matrices ending THERE is added

        for x in range(l):
            for y in range (w):
                if matrix[x][y] == 1:
                    if x == 0 or y == 0:
                        dp[x][y] = 1
                    else:
                        dp[x][y] = 1 + min(
                            dp[x-1][y],
                            dp[x][y-1],
                            dp[x-1][y-1]
                        )
                total += dp[x][y]

        return total
