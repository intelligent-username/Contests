# https://leetcode.com/problems/rotate-image/

# Complete

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # When rotating by 90 degrees, we have the "x and y coordinates switchede" and the final result reversed

        # Note that the matrix is n by n

        n = len(matrix)
        pose = n // 2

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for row in matrix:
            row.reverse()
