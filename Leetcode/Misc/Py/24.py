# https://leetcode.com/problems/reverse-integer/
# Easy edition (let's assume string conversion is allowed)
# In C++ I'll do the hard version.
# 24th 'misceallaneous' problem that I've done

class Solution:
    def reverse(self, x: int) -> int:
        sign = '-' if x < 0 else ''
        x = str(abs(x))

        temp = x[::-1]
        final = sign + temp
        integer = int(final)
        if integer > (2**31) - 1 or integer < -(2**31):
            return 0
        else:
            return integer

