# https://leetcode.com/problems/pascals-triangle/
# Complete

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]

        for i in range(numRows - 1):
            tmp = [0] + rows[-1] + [0]
            rows.append([tmp[j] + tmp[j+1] for j in range(len(rows[-1]) + 1)])

        return rows

