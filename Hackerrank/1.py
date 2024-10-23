# https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true
# Itertools practice

from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = list(product(A, B))

print(" ".join(map(str, result)))
