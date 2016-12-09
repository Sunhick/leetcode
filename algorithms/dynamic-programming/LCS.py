#!/usr/bin/python3

import numpy as np

str1 = "AGGTAB"
str2 = "GXTXAYB"

m, n = len(str1), len(str2)

dp = np.zeros((m+1, n+1), dtype=int)

for  i in range(1, m+1):
    for j in range(1, n+1):
        dp[i, j] = (dp[i-1, j-1]  + 1) if str1[i-1] == str2[j-1] else (max(dp[i-1, j], dp[i, j-1]))

print("LCS: \n", dp)
print("LCS =", dp[m, n])