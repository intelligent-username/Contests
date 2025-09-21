# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
# Took a while to get just right
# difficulty level - hard

class Solution(object):
    def largestRectangleArea(self, heights):
        n = len(heights)
        left = [0] * n   # indices of nearest smaller to left
        right = [n] * n  # indices of nearest smaller to right

        # compute left
        for i in range(n):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = left[p] - 1
            left[i] = p + 1

        # compute right
        for i in range(n-1, -1, -1):
            p = i + 1
            while p < n and heights[p] >= heights[i]:
                p = right[p]
            right[i] = p

        max_area = 0
        for i in range(n):
            width = right[i] - left[i]
            area = heights[i] * width
            max_area = max(max_area, area)

        return max_area


