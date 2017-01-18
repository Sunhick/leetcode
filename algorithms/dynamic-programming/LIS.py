#!/usr/bin/python3

import bisect

ar = [10, 22, 9, 33, 21, 50, 41, 60, 80]

s = []
l = 0

# N*log(N) for LIS
for e in ar:
    i = bisect.bisect_left(s, e)
    if (i == l):
        s.append(e)
        l += 1
    elif (i >=0 and i <= l):
        s[i] = e
    else:
        s.append(e)
        l += 1

print("LIS =", l)
print(s)
