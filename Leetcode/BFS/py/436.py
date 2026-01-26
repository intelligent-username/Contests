# https://leetcode.com/problems/island-perimeter

# Complete

from collections import deque

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        total = 0
        width, height = len(grid[0]), len(grid)

        seen = set()
        line = deque()

        looking = True

        while looking:
            for x in range(height):
                for y in range(width):
                    if grid[x][y]:
                        looking = False
                        line.append((x, y))
                        seen.add((x, y))
                        break
                if not looking:
                    break

        while line:
            x, y = line.popleft()

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < height and 0 <= ny < width:
                    if grid[nx][ny]:
                        if (nx, ny) not in seen:
                            seen.add((nx, ny))
                            line.append((nx, ny))
                    else:
                        total += 1
                else:
                    total += 1

        return total
