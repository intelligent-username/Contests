# https://leetcode.com/problems/zigzag-conversion/
# Zigzag conversion
# COMPLETE

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # String s
        # "Zigzagged" into n rows
        if numRows == 1:
            return s
        
        # Ignore the preamble I'm just thinking
        # --------------------------
        
        # Pattern:
        # 2 rows: no diagonal
        # 3 rows: 1 diagonal
        # 4 rows: 2 diagonals
        # 5 rows: 3 diagonals
        # and so forth

        # Let number of characters = n, num of rows = r
        # If no diagonals,
        # Number of columns = c = math.ceil(n/r) 
        # Now, factoring in the diagonals, we have n - 2 diagonal characters if n > 2
        # Number of diagonals is c - 2, c >= 2
        # So (c-2)(n-2) diagonal characters
        # But the characters so now we have c + c-2 columns
        # But this doesn't count # of characters taken from the columns
        # 
        # So ceil(n/r) columns
        # 

        # Basically, first row (i.e. the first x characters) has takes every cth character starting from 0.
        # Second row (i.e. the first x + cols // 2 characters) takes every cth character starting from 0 and 2 (in parallel)
        # Third row takes every cth character from 3
        # Fourth takes every cth from 4 and 6
        # Fifth takes every cth from 5 
        # and so on...

        # --------------
        
        newStr = ''

        lens = len(s)
        rows = [[] for x in range(numRows)] # Prep room for n rows
        pos = 0
        index = 0    # Which row to add to 
        down = True  # added

        while pos < lens:
            rows[index].append(s[pos])
            pos += 1
            if index == 0:
                down = True # If we're at the top, start going down
            elif index == numRows - 1:
                down = False # If we're at the bottom, start going up (diagonal)
            
            index += 1 if down else -1  # changed

        # Now the rows are ready
        for x in rows:
            newStr += ''.join(x)

        return newStr
