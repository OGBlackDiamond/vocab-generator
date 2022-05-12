import requests
from bs4 import BeautifulSoup

def synnant(term, type = 0):
    response = requests.get('https://www.thesaurus.com/browse/{}'.format(term))
    soup = BeautifulSoup(response.text, 'html.parser')
    soup.find('section', {'class': 'css-1ofzyv e1ccqdb60'})
    #Getting the synonyms
    synlist = [span.text for span in soup.findAll('a', {'class': 'css-1kg1yv8 eh475bn0'})]
    #Getting the antonyms
    antlist = [span.text for span in soup.findAll('a', {'class': 'css-15bafsg eh475bn0'})]
    if synlist and antlist != []:
        synlist.insert(0, "Synonym")
        antlist.insert(0, "Antonym")
        if type == 1:
            return synlist[:2]
        elif type == 2:
            return antlist[:2]
        else:
            return synlist[:2] + antlist[:2]
    else:
        return term + " does not not have a synonym or antonym in the API! \nCheck spelling and if it can be found at thesaurus.com!"
