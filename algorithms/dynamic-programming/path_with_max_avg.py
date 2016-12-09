#!/usr/bin/python3

import numpy as np

mat = np.array([[1, 2, 3],
                [6, 5, 4],
                [7, 3, 9]])

m, n = mat.shape

dp = np.zeros((m+1, n+1), dtype = int)


for i in range(1, m+1):
    for j in range(1, n+1):
        dp[i, j] = max(dp[i-1, j], dp[i, j-1]) + mat[i-1, j-1]

# print("dp: \n", dp, end="\n\n")
print("Max avg=", dp[m][n]/(m+n-1))