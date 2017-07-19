#!/usr/bin/python
# Check for valid parathensis

def valid_paranthesis(expression):
    map = {']':'[', ')':'(' ,'}':'{'}
    st = []
    for literal in expression:
        if literal in map.values():
            st.append(literal)
        if literal in map.keys():
            if st == []:
                return False
            popped = st.pop()
            if popped != map[literal]:
                return False
    return st == []

def valid_para_opt(s):
    st = []
    for literal in s:
        if literal == "(":
            st.append(")")
        elif literal == "[":
            st.append("]")
        elif literal == "{":
            st.append("}")
        elif literal in ")]}":
            if st == [] or st.pop() != literal:
                return False
    return st == []

if __name__ == "__main__":
    s = "() (() [()])"
    print valid_para_opt(s)

