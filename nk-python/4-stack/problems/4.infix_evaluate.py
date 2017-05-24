#!/usr/bin/python
# Evaluate an infix expression in a single pass using 2 stacks

from stacklist import *

def evaluate(infix):
    stk_operands = Stack()
    stk_operators = Stack()
    prec = {"^": 4,
            "*": 3,
            "/": 3,
            "+": 2,
            "-": 2,
            "(": 1
            }
    for literal in infix:
        if literal.isdigit():
            stk_operands.push(float(literal))
        elif literal in prec.keys():
            if stk_operators.isEmpty() or literal == "(":
                stk_operators.push(literal)
            else:
                while not stk_operators.isEmpty() and prec[literal] <= prec[stk_operators.peek()]:
                    num = solve(stk_operands.pop(), stk_operands.pop(), stk_operators.pop())
                    stk_operands.push(num)
                stk_operators.push(literal)
        elif literal == ")":
            while 1:
                popped = stk_operators.pop()
                if popped == "(":
                    break
                num = solve(stk_operands.pop(), stk_operands.pop(), popped)
                stk_operands.push(num)
    while not stk_operators.isEmpty():
        num = solve(stk_operands.pop(), stk_operands.pop(), stk_operators.pop())
        stk_operands.push(num)
    return stk_operands.peek()

def solve(b,a,op):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        return a/b
    #else:
    #    return a^b


if __name__ == "__main__":
    infix = "(1+4)*8/5"
    print evaluate(infix)