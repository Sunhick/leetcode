#!/usr/bin/python3

stack = [30, -5, 44, -56, 7 ,18, 14, -3, 0, 99, -99]

def sortstack(stack):
    if len(stack) == 1:
        return
    a = stack.pop()
    if not stack:
        return

    sortstack(stack)
    b = stack.pop()
    if a > b:
        stack.append(b)
        stack.append(a)
    else:
        stack.append(a)
        sortstack(stack)
        stack.append(b)

sortstack(stack)
print(stack)

