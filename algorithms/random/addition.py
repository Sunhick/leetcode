#!/usr/bin/python3

def Add(x, y):
    while y!=0:
        carry = x&y
        x = x^y
        y = carry << 1
    return x

def main():
    print("Sum = ", Add(7, 7))

if __name__ == '__main__':
    main()