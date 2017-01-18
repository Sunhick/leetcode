#!/usr/bin/python3

import numpy as np

from math import ceil

def main():
    mat = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]])

    m, n = mat.shape

    for ring in range(0, ceil(min(m/2, n/2))):
        anticlock_rotate(mat, ring)

def anticlock_rotate(mat, ring):
    row, col = mat.shape
    dim = (row - 2*ring, col - 2*ring)
    for re in range(ring, row - ring):
        spiral_swap(mat, (ring, re), dim)

def spiral_swap(mat, loc, dim):
    row, col = loc
    row = row - row
    col = col - row


if __name__ == '__main__':
    main()