#!/usr/bin/python
#Finds if a word can be typed by the keys in the same row

def keyboard_row_less_optimized(words):
    first_row = set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
    second_row = set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'])
    third_row = set(['z', 'x', 'c', 'v', 'b', 'n', 'm'])
    collection = []
    for word in words:
        if word == "":
            continue
        flag = [0]*3
        for alphabet in word.lower():
            if flag[0] == 0:
                if alphabet not in first_row:
                    flag[0] = 1
            if flag[1] == 0:
                if alphabet not in second_row:
                    flag[1] = 1
            if flag[2] == 0:
                if alphabet not in third_row:
                    flag[2] = 1
        for digit in flag:
            if digit == 0:
                collection.append(word)
                break
    return collection

def keyboard_row(words):
    keyboard_layout = ["qwertyuiop","asdfghjkl","zxcvbnm"]
    map = {}
    collection = []
    for i in range(len(keyboard_layout)):
        for alphabet in keyboard_layout[i]:
            map[alphabet] = i
    for word in words:
        if word == "":
            continue
        if word[0].lower() in map:
            index = map[word[0].lower()]
        else:
            continue
        for i in range(1,len(word)):
            if map[word[i].lower()] != index:
                index = -1
                break
        if index != -1:
            collection.append(word)
    return collection


if __name__ == "__main__":
    words = ["Hello","Alaska","Dad","Peace"]
    print keyboard_row(words)
