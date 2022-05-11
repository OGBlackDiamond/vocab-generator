from synnant import *
from PyDictionary import PyDictionary
dictionary = PyDictionary()

raw_word = input()
Word = raw_word.lower()

def get_word_def(word):
    try:
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
    except:
        return "That word does not have a definition in the API! \nCheck spelling or its existance in Dictionary.com"

def get_syn_ant(word, type = ""):
    antstart = -1
    words = synnant(word, type)
    if "Antonyms" in words:
        antstart = words.index("Antonyms")    

    return str(words[0: antstart])[1:-1] + "\n" + str(words[antstart:])[1:-1]
        
    
    

    
    



if Word != "":
    print(get_word_def(Word))
    print(get_syn_ant(Word))
        
