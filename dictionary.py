from PyDictionary import PyDictionary
from synonym import *
dictionary = PyDictionary()

raw_word = input()
Word = raw_word.lower()


def get_word_def(word):
    definition = dictionary.meaning(word)
    
    if "Noun" in definition:
        noun = "Noun: \n" + str(definition["Noun"])[1:-1] + "\n"
    else: 
        noun = ""

    if "Verb" in definition:
        verb = "Verb: \n" + str(definition["Verb"])[1:-1] + "\n"
    else:
        verb = ""

    if "Adjective" in definition:
        adjective = "Adjective: \n" + str(definition["Adjective"])[1:-1] + "\n'"
    else:
        adjective = ""

    return noun + verb + adjective

def get_syn_ant(word):
    synonym = synonyms(word)

    print(synonym + antonym)
    
    


while True:
    if Word != "":
        print()
        
