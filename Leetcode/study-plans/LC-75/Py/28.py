# https://leetcode.com/problems/dota2-senate

# Senate voting problem

# Complete

from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        
        # The optimal strategy is just to ban all 'next' senators
        # Then to facilitate looping back, add the length to the pushed item on the queue

        R = deque()
        D = deque()

        length = len(senate)

        for i in range(length):
            c = senate[i]
            if c == 'R':
                R.append(i)
            else:
                D.append(i)

        while R and D:
            r = R.popleft()
            d = D.popleft()
            if d < r:
                D.append(d + length)
            else:
                R.append(r + length)
        
        return 'Radiant' if R else 'Dire'
