#!/usr/bin/python
#Check if the palindrome is valid

def isPalindrome(sentence):
    i = 0
    j = len(sentence)-1
    while i<j:

        while not sentence[i].isalnum():
            i += 1
        while not sentence[j].isalnum():
            j -= 1
        if sentence[i].lower() != sentence[j].lower():
            return False
        i += 1
        j -= 1
    return True

if __name__ == "__main__":
    sentence = "A man, a plan, a canal: Panama"
    print isPalindrome(sentence)