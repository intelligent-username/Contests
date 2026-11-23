# https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=leetcode-75
# Product of Array Except Self

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        answer = [1] * n
        left_prod = 1
        for i in range(n):
            answer[i] = left_prod
            left_prod *= nums[i]
        
        right_prod = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_prod
            right_prod *= nums[i]
        
        return answer
