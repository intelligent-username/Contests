# https://leetcode.com/problems/design-task-manager/description/

# This was a daily problem
# Took me way too long


import heapq
# Note: Python's built-in heap uses min-heap by default. That's why we store negative values for prioririty.

class TaskManager(object):
    def __init__(self, tasks):
        self.tasks = {}  # taskId -> [userId, priority]
        self.heap = []   # max-heap: (-priority, -taskId, taskId)
        for userId, taskId, priority in tasks:
            self.tasks[taskId] = [userId, priority]
            heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def add(self, userId, taskId, priority):
        self.tasks[taskId] = [userId, priority]
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId, newPriority):
        self.tasks[taskId][1] = newPriority
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId):
        if taskId in self.tasks:
            del self.tasks[taskId]

    def execTop(self):
        while self.heap:
            neg_priority, neg_taskId, taskId = heapq.heappop(self.heap)
            if taskId in self.tasks and self.tasks[taskId][1] == -neg_priority:
                userId, _ = self.tasks.pop(taskId)
                return userId
        return -1
