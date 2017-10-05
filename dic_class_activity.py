#imports arvg from system to accept user input
from sys import argv
#creats a variable that stores user input
user_input = input("please enter a word and i will show you what the word is composed of \n >")
#create an empty dictionary data type
word = dict()
#loops though each letter of the user input and stores the current letter in i
for i in user_input:
    #if i is a key in the dictionary = TRUE do this
    if i in word:
        #addes the value of the current key by one
        word[i] += 1

    else:
        #add a new key
        word[i] = 1

print (f"the word composes of the these letters and appears this many times:\n ")
for i in word:
     print(f"the letter {i} appears {word[i]} time(s) \n")
