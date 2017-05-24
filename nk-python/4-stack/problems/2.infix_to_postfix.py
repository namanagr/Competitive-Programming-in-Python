#!/usr/bin/python
#Infix to postfix expression converter

from stacklist import *

def infix2postfix(infix):
    stk = Stack()
    prec = {"^":4,
            "*":3,
            "/":3,
            "+":2,
            "-":2,
            "(":1
            }
    output = ""
    for literal in infix:
        if literal.isalnum(): # If operand, append it to the output expression
            output += literal
        elif literal in prec.keys(): # If literal contains an operator or bracket
            if stk.isEmpty() or literal == "(": # Empty stack case
                stk.push(literal)
                continue
            while not stk.isEmpty() and prec[literal] <= prec[stk.peek()]: # Precedence of literal is less than top
                output += stk.pop() # In that case, pop out the top element and append it to output expression.
            stk.push(literal)
        elif literal == ")":
            while 1: # Pop and append operators to the output expression till "("
                popped = stk.pop()
                if popped == "(":
                    break
                output += popped
    while not stk.isEmpty(): # Pop out the remains elements of the stack and append to the output expression.
        output += stk.pop()
    return output

if __name__ == "__main__":
    #infix = "A*B-(C+D)+E"
    infix = "a+b*(c^d-e)^(f+g*h)-i"
    print infix2postfix(infix)
