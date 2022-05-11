 
"""
Created on Mon Oct  8 20:19:00 2018

@author: BH
"""
import requests
from bs4 import BeautifulSoup
import bs4
Word = "hard"
class SynAntDictionary(object):
    #@staticmethod
    def synonym(Word):
        print(Word)
        if len(Word.split()) > 1:
            print("Error: A Term must be only a single word")
        else:
            try:
                data = requests.get("http://www.thesaurus.com/browse/" + Word)
                Selection = BeautifulSoup(data.text,"lxml")
                print(data.text)
                Synterms=Selection.find(class_="postab-container css-1nq2eka e9i53te1").find_all("strong")
                "Filter and format Syn Terms into Comma Delineated String"
                t=0
                while t < len(Synterms):
                    if t == 0:
                        SynList=Synterms[t]
                    else:
                        SynList= str(SynList) + "," + str(Synterms[t])
                    t=t+1
                SynList = SynList.replace("<strong>", "")
                SynList = SynList.replace("</strong>", "")
                SynList = SynList.replace(", ", ",")
                print(SynList)
                
                return SynList
            except:
                print(str(Word) +" has no Synonyms in the API")
                
                
    #@staticmethod
    def antonym(Word):
        if len(Word.split()) > 1:
            print("Error: A Term must be only a single word")
        else:
            try:
                data = requests.get("http://www.thesaurus.com/browse/" + Word)
                SelectionAnt=BeautifulSoup(data.text,"lxml")
                Antterms=SelectionAnt.find(class_="antonyms-container css-7jbvqm e1991neq0").find(class_="css-1lc0dpe et6tpn80").find_all("a")
                "Filter and format Ant Terms into Comma Delineated String"
                t=0
                while t < len(Antterms):
                    if t == 0:
                        AntList=Antterms[t].get_text()
                    else:
                        AntList= str(AntList) + "," + str(Antterms[t].get_text())
                    if t==10:
                        t=len(Antterms)
                    t=t+1
                print(AntList)
                return AntList
                
            except:
                print(str(Word) + " has no Antonyms in the API")


    synonym(Word)