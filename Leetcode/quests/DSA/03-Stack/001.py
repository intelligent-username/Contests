# https://leetcode.com/problems/build-an-array-with-stack-operations
# Done

class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        push = "Push"
        pop = "Pop"
        ans = []
        
        i = 0
        value = 1
        while i < len(target):
            ans.append(push)
            if target[i] == value:
                i += 1
            else:
                ans.append(pop)
            value += 1


        return ans
