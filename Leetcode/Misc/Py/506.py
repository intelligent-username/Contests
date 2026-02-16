# https://leetcode.com/problems/relative-ranks/

# Complete

# Implementing a heap from scratch by far took the most time but I was doing this in preparation for a test

from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Plan:
        #   Construct a max-heap by score (so highest score at root)
        #       Within the heap, also store the index 'i' of each athlete
        #       Which'll be the original position of the athlete in 'score'
        #   Then, constantly pop from the heap
        #       Keep track of which index we're popping,
        #       this way we know we're at rank k, for example
        #       At each pop, take the rank at write it to that position
        #       so we know what rank k the athlete as position i had.

        # And that's why this problem is ranked 'easy'

        heapSize = 0
        
        def sift(pos: int):
            parent = (pos - 1) // 2

            if pos == 0:
                return
            elif sortScores[pos][0] > sortScores[parent][0]:
                sortScores[pos], sortScores[parent] = \
                        sortScores[parent], sortScores[pos]
                sift(parent)
            

        def sink(pos: int):
            left = 2 * pos + 1
            right = 2 * pos + 2
            largest = pos
            if left < heapSize and sortScores[left][0] > sortScores[largest][0]:
                largest = left
            if right < heapSize and sortScores[right][0] > sortScores[largest][0]:
                largest = right
            if largest != pos:
                sortScores[pos], sortScores[largest] = sortScores[largest], sortScores[pos]
                sink(largest)

            
        def heapPop():
            nonlocal heapSize
            if heapSize == 0:
                return None

            val = sortScores[0]
            sortScores[0] = sortScores[heapSize - 1]
            heapSize -= 1
            sortScores.pop()
            sink(0)

            return val

        sortScores = []

        length = len(score)

        for i in range(length):
            # Remember, 'i' right now is the ORIGINAL position
            heapSize += 1
            sortScores.append((score[i], i))
            sift(i)


        ans = [""] * length        
        # "Gold Medal", "Silver Medal", "Bronze Medal"

        for x in range(1, length + 1):
            tupp = heapPop()
            if x == 1:
                ans[tupp[1]] = "Gold Medal"
            elif x == 2:
                ans[tupp[1]] = "Silver Medal"
            elif x == 3:
                ans[tupp[1]] = "Bronze Medal"
            else:
                ans[tupp[1]] = str(x)

        return ans
