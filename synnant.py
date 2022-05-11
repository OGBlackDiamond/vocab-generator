import requests
from bs4 import BeautifulSoup

def synnant(term, type):
    response = requests.get('https://www.thesaurus.com/browse/{}'.format(term))
    soup = BeautifulSoup(response.text, 'html.parser')
    soup.find('section', {'class': 'css-17ofzyv e1ccqdb60'})
    #Getting the synonyms
    synlist = [span.text for span in soup.findAll('a', {'class': 'css-1kg1yv8 eh475bn0'})]
    #Getting the antonyms
    antlist = [span.text for span in soup.findAll('a', {'class': 'css-15bafsg eh475bn0'})]
    if synlist and antlist != []:
        synlist.insert(0, "Synonyms")
        antlist.insert(0, "Antonyms")
        if type == "syn":
            return synlist
        elif type == "ant":
            return antlist
        else:
            return synlist + antlist
    else:
        return "That word does not exist in the API! \nCheck spelling and if it can be found at thesaurus.com!"
