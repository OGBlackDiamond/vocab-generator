from dictionary import *
from run import *
from usedinacentence import *
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
        if ("Synonym" in syns) or ("Antonym" in ants):
            syns_list.append(syns)
            ants_list.append(ants)
            print("Prog: Success!")
        else:
            print("Prog: Synonyms or Antonyms for " + word + " failed!")

    return [syns_list, ants_list]


def get_usages(wordslist):
    usageslist = []
    for word in wordslist:
        print("Prog: Getting usage in sentence for " + word)
        use = usages(word)
        if "Usage in a Sentence:" in use:
            usageslist.append(use)
            print("Prog: Success")
        else:
            print("Usages for " + word) + " failed!"
    return usageslist



def format():
    wordList = comp_word_list()
    if Finished == True:
        defs = get_defs(wordList)
        synsants = get_synant(wordList)
        uses = get_usages(wordList)
        count = -1
        for words in defs:
            count += 1
            output_file.writelines(["\n", wordList[count].capitalize(), "\n", words, "\n", str(synsants[0][0])[1:-1], "\n", str(synsants[1][count])[1:-1], "\n", str(uses[count][0]), "\n", str(uses[count][1:2])[1:-1]])
    
    
    



while Finished != True:
    format()




