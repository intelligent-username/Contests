# https://leetcode.com/problems/3sum/submissions/
# Complete

# Most of the work here is with the duplicates but otherwise it's a simple two-pointer problem


from ast import List # Just to get rid of VSCode linting errors etc.


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # First sort the array
        nums.sort()
        sols = []

        # Then, with this sorted array, iterate through all variables, with each one getting it's own sliding window.
        # We need all the ones that add up to zero.

        length = len(nums)

        for i in range(length-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue # This'll create a duplicate tuple, no need. Note, array is sorted. 
            p1 = i + 1
            p2 = length - 1
            curr = nums[i]

            while p1 < p2:
                # First (smaller) and second (bigger) numbers. Note that curr is smallest.
                n1, n2 = nums[p1], nums[p2]

                total = n1 + n2 + curr

                if total == 0:
                    sols.append([curr, nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1
                    # Skip duplicates after a match
                    while p1 < p2 and nums[p1] == nums[p1 - 1]:
                        p1 += 1
                    while p2 > p1 and nums[p2] == nums[p2 + 1]:
                        p2 -= 1

                elif total < 0:
                    # Too small, so we need bigger numbers.
                    # Remember list is sorted, so increment lower bound
                    p1 += 1
                else: # Too large, decremenet upper bound
                    p2 -= 1
            
        return sols
