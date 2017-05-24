#!/usr/bin/python
# Evaluate a postfix expression

import cv2
from stacklist import *

def postfix_eval(expression):
    stk = Stack()
    for literal in expression:
        if literal.isalnum():
            stk.push(literal)
        elif literal in "*/+-^":
            num = solve(stk.pop(),stk.pop(),literal)
            stk.push(num)
    return stk.pop()

def solve(a,b,op):
    a = int(a)
    b = int(b)
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        return a/b
    else:
        return a^b

if __name__ == "__main__":
    po_expression = "123*+5-"
    print postfix_eval(po_expression)