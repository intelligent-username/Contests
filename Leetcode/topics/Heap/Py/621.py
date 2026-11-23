# https://leetcode.com/problems/task-scheduler/

# Complete

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # I think a greedy algorithm would work
        # reqs = {}
        # cooldowns = {}
        
        # for x in tasks:
        #     cooldowns[x] = 0
        
        # while tasks:
        #       # nah inefficient

        cur = 0
        reqs = {}

        for x in tasks:
            if x in reqs:
                reqs[x] += 1
            else:
                reqs[x] = 1

        # Stores which ones are READY
        pq = []

        for x in reqs:
            heappush(pq, -reqs[x])

        cooldowns = deque()

        while pq or cooldowns:
            cur += 1

            if pq:
                left = -heappop(pq)
                left -= 1

                if left > 0:
                    cooldowns.append((cur + n, left))

            if cooldowns and cooldowns[0][0] == cur:
                tr, left = cooldowns.popleft()
                heappush(pq, -left)

        return cur
