# https://leetcode.com/problems/kth-largest-element-in-a-stream

# Complete

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.items = nums
        heapify(self.items)
        while len(self.items) > k:
            heappop(self.items)

    def add(self, val: int) -> int:
        heappush(self.items, val)
        if len(self.items) > self.k:
            heappop(self.items)
        return self.items[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
