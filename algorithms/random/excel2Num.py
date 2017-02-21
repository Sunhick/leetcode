#!/usr/bin/python3

import math

def excel2Num(colName):
    r = 0
    for i, e in enumerate(colName[::-1]):
        r += (ord(str(e))-64)*int(math.pow(26, i))
    return r

def Num2excel(colNum):
    print(colNum)
    r = ""
    while colNum > 0:
        r = chr(64+1+(colNum-1)%26) + r
        colNum = (colNum-1)//26
    return r

def main():
    print(excel2Num("AB"))
    print(Num2excel(excel2Num("AZ")))

if __name__ == "__main__":
    main()