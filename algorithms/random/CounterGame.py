#!/usr/bin/python3

def WhoWins(N):
    turn = 0 
    while(N != 1):
        if N % 2 == 0:
            N = N >> 1
            turn += 1
        else:
            largest = 1 #largest power of 2
            while(largest<<1 < N):
                largest = largest << 1
            N -= largest
            turn += 1
    return "Richard" if turn%2==0 else "Louise"

def main():
    n = int(input())
    for i in range(n):
        N  = int(input())
        name = WhoWins(N)
        print(name)

if __name__ == '__main__':
    main()