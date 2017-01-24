#!/usr/bin/python3

stocks = [10, 4, 5, 90, 120, 80, 67, 7,8,9,0,0,88,7,55,6,6,33,4,455,6,7,778]

stack = list()
spans = [1]*len(stocks)

stack.append(0)

for i in range(1, len(stocks)):
    val = stocks[i]
    while (stack and stocks[stack[-1]] <= val):
        stack.pop()

    spans[i] = (i+1) if not stack else (i-stack[-1])
    stack.append(i)

print('Spans = ', spans)
print('Stack = ', stack)