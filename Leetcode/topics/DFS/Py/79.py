# https://leetcode.com/problems/word-search/description/?envType=problem-list-v2&envId=depth-first-search

# Literally took an hour to do cleanly :(

# Complete

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # Have to implement iteratively since Leetcode
        # doesn't let me change the arguments

        # givena n mxn grid
        # so m rows and n columns are filled in (by Pre)

        m = len(board)          # ROWS
        n = len(board[0])       # COLUMNS

        length = len(word)

        def dfs(x, y, pos, seen):
 

            if (x < 0 or y < 0 \
                or x >= m or y >= n):
                return False

            # Otherwise we get to work

            if (x,y) in seen:
                return False
            
            if (board[x][y] == word[pos]):

                if pos == length - 1:
                    return True

                seen.add((x,y))

                # INDUCTIVE HYPOTHESIS ALERT

                rest_found =    dfs(x+1, y, pos + 1, seen) or \
                                dfs(x-1, y, pos + 1, seen) or \
                                dfs(x, y+1, pos + 1, seen) or \
                                dfs(x, y-1, pos + 1, seen)

                seen.remove((x,y))
                
                if rest_found:
                    return True
            
            return False


        if m * n < length:
            return False

        # Let the position of a letter be represented as (x,y), where top left is (0,0)
        # And as we move down and right x and y increase

        # The neighbours of each word are (x+1, y), (x, y+1), (x-1, y), (x, y-1) [within bounds]

        p = 0   # Current position of the word

        seen = set()
        for i in range(m):
            for j in range(n):
                # Empty seen?
                if board[i][j] == word[0]:
                    if dfs(i, j , p, seen):
                        return True
                    seen.clear()
        
        return False
