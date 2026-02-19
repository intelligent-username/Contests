# https://leetcode.com/problems/kth-largest-element-in-an-array

# Complete

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapify(nums)

        # temp = []
        for i in range(k):
            s = heappop(nums)

        # We could've stored in the list `temp` and then restored everything but that's not needed
        
        return -s

        # It looks like the "canonical" solution is to keep a min-heap of size k
        # No need to modify the numbers to negative, etc.

        # When building a min-heap of size k, we pop once the size exceeds k,
        # Which is to say, we get rid of the smallest element once the size exceeds k
        # This'll then re-heapify and we'll push to the heap again.
        # We'll keep popping the smallest as the size exceeds k
        # Effectively, by the end of it, we're left with the k largest elements from the list.

        # Thus the root would be the k-th smallest element. Smart.

        # Could also just
        #         return(sorted(nums, reverse=True)[k-1])

