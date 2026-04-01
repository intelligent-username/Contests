# https://leetcode.com/problems/spiral-matrix-ii/

# Complete
# Very annoying question

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # n by n grid
        grid = [[0] * n for x in range(n)]

        # navigate around it
        
        x1, x2, y1, y2, val = 0, n - 1, 0, n - 1, 1

        while x1 <= x2 and y1 <= y2:
            for c in range(y1, y2 + 1):
                grid[x1][c] = val
                val += 1
            for r in range(x1 + 1, x2 + 1):
                grid[r][y2] = val
                val += 1
            for c in range(y2 - 1, y1 - 1, -1):
                grid[x2][c] = val
                val += 1
            for r in range(x2 - 1, x1, -1):
                grid[r][y1] = val
                val += 1
            x1, x2, y1, y2 = x1 + 1, x2 - 1, y1 + 1, y2 - 1
        
        return grid
