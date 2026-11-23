# https://leetcode.com/problems/unique-paths/

# Complete

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # So this can be something like a sublist sum
        # The only way to reach any given poisition is the number of ways to reach:
            # The cell to it's left
            # The cell above it
            # Added together
        
        # In every other case, it depends

        if (m == 1 and n == 1):
            return 1
        
        # m rows, n columns 
        times = [[0] * n for _ in range(m)]

        times[0] = [1] * n
        for i in times:
            i[0] = 1

        # i.e. the first row and column are purely ones

        for x in range(1, m):
            for y in range(1, n):
                times[x][y] = times[x-1][y] + times[x][y-1]

        return times[m-1][n-1]

