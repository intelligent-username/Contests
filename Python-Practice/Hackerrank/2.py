# https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true

import numpy as np

N = int(input())

matrix = []

for _ in range(N):
    matrix.append(list(map(float, input().split())))

# Calculate the determinant and round to 2 decimal places
determinant = np.linalg.det(matrix)
print(round(determinant, 2))
