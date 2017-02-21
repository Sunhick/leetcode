#!/usr/bin/python3

def bmin(x, y, z):
    i = 0
    while (x and y and z):
        x -= 1
        y -= 1
        z -= 1
        i += 1
    return i

def bmax(x, y, z):
    i = 0
    while (x or y or z):
        x -= 1
        y -= 1
        z -= 1
        i += 1

def main():
    mi = bmin(23,45,78)
    #ma = bmax(23,45,78)
    print("min = ", mi)
    # print("max = ", ma)

if __name__ =='__main__':
    main()