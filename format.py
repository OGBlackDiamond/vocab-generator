from dictionary import *
from run import *


Word = ""
defs = ""
WordList = []
Finished = False
output_file = open("output.txt", "w")

def get_defs(wordslist):
    for word in wordslist:
        print("Prog: Getting definitions for " + word)
        defs = get_word_def(word)
        if word not in defs:
            print("Prog: Success!")
        else:
            print("Prog: Definitions for " + word + " failed!")

        return defs


def comp_word_list():
    global Finished
    Word = input().lower()
    if Word != "" and Word != "prog end":
        WordList.append(Word)
        print("Prog: Added " + Word + " as a new word! Enter a new word or type 'prog end' to end your list!")
    elif Word == "prog end":
        Finished = True
        print("Prog: List compilation complete! \nStarting processing...")

    return WordList

def format():
    wordList = comp_word_list()
    if Finished != True:
        defs = get_defs(wordList)
        output_file.writelines([defs, "\n"])
    
    
    



while Finished != True:
    format()




