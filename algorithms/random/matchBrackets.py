def hasBalancedBrackets(str):
    brackets = {'(':')', '{':'}', '[':']', '<':'>'}
    
    stack = list()
    for each in str:
        # has to be a valid brackets to be pushed on stack, otherwise ignore.
        if (each not in brackets.keys() and each not in brackets.values()):
            # print 'ignore ', each
            continue
        # print each
        if not stack:
            stack.append(each)
            continue
        top = stack[-1]
        if (top in brackets.keys() and brackets[top] == each):
            stack.pop()
            continue
        else:
            stack.append(each)
            
    ret = 1 if not stack else 0
    return ret
