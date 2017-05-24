#!/usr/bin/python
# Check for valid parathensis

from stacklist import *

class stack(Stack):
    def valid_paranthesis(self, expression):
        dict = {']':'[','}':'{',')':'('}
        for literal in expression:
            if literal in dict.values():
                self.push(literal)
            elif literal in dict.keys():
                if self.isEmpty():
                    return False
                popped = self.pop()
                if popped != dict[literal]:
                    return False
        if self.isEmpty():
            return True
        return False

if __name__ == "__main__":
    expression = "() (() [()])"
    s = stack()
    print s.valid_paranthesis(expression)


