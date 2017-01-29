#!/usr/bin/python3

def Distance(T, k, dist):
    if T[k] == k:
        dist[k] = 0
        return dist
    if dist[k] == -1:
        q = T[k]
        dist = Distance(T, q, dist)
        dist[k] = 1 + dist[q]
        return dist
    return dist

def solution(T):
    M = len(T)
    dist = [-1] * M
    for i in range(M):
        if dist[i] == -1:
            k = T[i]
            dist = Distance(T, k, dist)
            dist[i] = 1 + dist[k]

    counter = [0] * M
    for e in dist:
        if e <= 0 : continue
        counter[e-1] += 1
    return counter

T = [9, 1, 4, 9, 0, 4, 8, 9, 0, 1]
dist = solution(T)
print(dist)