#!/usr/bin/python
#Given a word, you need to judge whether the usage of capitals in it is right or not.
#We define the usage of capitals in a word to be right when one of the following cases holds:
#All letters in this word are capitals, like "USA".
#All letters in this word are not capitals, like "leetcode".
#Only the first letter in this word is capital if it has more than one letter, like "Google".
#Otherwise, we define that this word doesn't use capitals in a right way.

def detect_capital(word):
    capital_count = 0
    for alphabet in word:
        if alphabet.isupper():
            capital_count += 1
    if capital_count == len(word):
        return True
    elif capital_count == 1 and word[0].isupper():
        return True
    elif capital_count == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    word = "sDD"
    print word, detect_capital(word)
