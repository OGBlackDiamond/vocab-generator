from dictionary import *
from run import *
print("Input words here!")

Word = ""
defs = ""
WordList = []
Finished = False
output_file = open("output.txt", "w")




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



def get_defs(wordslist):
    global defsList
    defsList = []
    for word in wordslist:
        print("Prog: Getting definitions for " + word)
        defs = get_word_def(word)
        if word not in defs:
            print("Prog: Success!")
            defsList.append(defs)
        else:
            print("Prog: Definitions for " + word + " failed!")

    return defsList


def get_synant(wordslist):
    syns_list = []
    ants_list = []
    for word in wordslist:
        print("Prog: Getting Synonyms and Anytonyms for " + word)
        syns = synnant(word, 1)
        ants = synnant(word, 2)
        if ("Antonym" in ants):
            ants_list.append(ants)
            print("Prog: Success!")
        else:
            ants_list.append("-no_ants-")
            print("Prog: Antonyms for " + word + " failed!")

        if ("Synonym" in syns):
            syns_list.append(syns)
            print("Prog: Success!")
        else:
            syns_list.append("-no_syns-")
            print("Prog: Synonyms for " + word + " failed!")

    return [syns_list, ants_list]


def format():
    wordList = comp_word_list()
    if Finished == True:
        defs = get_defs(wordList)
        synsants = get_synant(wordList)
        count = 0
        for words in defs:
            count += 1
            output_file.writelines(["\n", wordList[count - 1].capitalize(), "\n", words, "\n", str(synsants[0][0])[1:-1], "\n", str(synsants[1][count -1])[1:-1], "\n"])

while Finished != True:
    format()


