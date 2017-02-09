#!/usr/bin/python3

"""
A ^ A = 0
0 ^ A = A
"""
def findOnce(*args):
    xor = 0
    for e in args:
        xor ^= e
    return xor

def main():
    print(findOnce(1,2,3,4,5,4,3,2,1))

if __name__ == "__main__":
    main()