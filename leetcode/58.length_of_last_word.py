#!/usr/bin/python
# This program returns the length of the last word

def len_last_word(s):
    if s == "":
        return 0
    words = s.split(" ")
    no_of_words = len(words)
    return len(words[no_of_words-1])

if __name__ == "__main__":
    s = "Hello World"
    print len_last_word(s)