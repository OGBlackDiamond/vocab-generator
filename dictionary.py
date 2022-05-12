from synnant import *
from PyDictionary import PyDictionary
dictionary = PyDictionary()

#Gets the definitions of the word using PyDictionary
def get_word_def(word):
    try:
        definition = dictionary.meaning(word)
        #Checks the types of definitions given
        if "Noun" in definition:
            noun = "Noun: \n" + str((definition["Noun"])[: 2])[1:-1] + "\n"
        else: 
            noun = ""

        if "Verb" in definition:
            verb = "Verb: \n" + str((definition["Verb"])[: 2])[1:-1] + "\n"
        else:
            verb = ""

        if "Adjective" in definition:
            adjective = "Adjective: \n" + str((definition["Adjective"])[: 2])[1:-1] + "\n'"
        else:
            adjective = ""


        #Returns the formatted text
        return noun + verb + adjective
    except:
        return word +  " does not have a definition in the API! \nCheck spelling or its existance in Dictionary.com"

#Gets the synonyms and antonyms
def get_syn_ant(word, type = ""):
    antstart = -1
    words = synnant(word, type)
    if "Antonyms" in words:
        antstart = words.index("Antonyms")    

    return str(words[0: antstart])[1:-1] + "\n" + str(words[antstart:])[1:-1]

