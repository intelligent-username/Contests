# https://leetcode.com/problems/min-cost-climbing-stairs/

# Complete

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Interesting

        # So I need the cheapest way to reach position n = [len(cost) - 1]
        # Which is the minimum of the minimum cost for reaching n-1 or n-2
            # n-1 is the min of reaching n-2 and n-3
            # And n-2 is the min of reaching n-3 and n-4
            # Notice how a lot of this is reused. So dynamic programming.
        # pos[i] = min(reaching([i-1]) + cost[i-1], reaching(i-2) + cost[i-2])

        # Wrong btw
        
        # if len(cost) == 1 or len(cost) == 2:
        #     return 0
        min_costs = [0, 0]

        n = len(cost)
        for i in range(2, n+1):
            min_costs.append(min(
                cost[i-1] + min_costs[i-1], cost[i-2] + min_costs[i-2]
            ))
        
        return min_costs[n]
