#!/usr/bin/python3

from numpy import inf

floors = 300
eggs = 3

dp = [[0 for i in range(floors+1)] for j in range(eggs+1)]

dp[1:2] = [range(floors+1)]

for egg in range(2, eggs+1):
    for floor in range(2, floors+1):
        mtries = inf
        for i in range(floor, 0, -1):
            tries = 1 + max(dp[egg-1][i-1], dp[egg][floor-i])
            mtries = min(mtries, tries)
        dp[egg][floor] = mtries

print("Max tries = ", dp[eggs][floors])