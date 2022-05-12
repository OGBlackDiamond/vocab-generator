import requests
from bs4 import BeautifulSoup

def usages(term):
    term = term
    response = requests.get("https://www.dictionary.com/browse/{}".format(term))
    soup = BeautifulSoup(response.text, "html.parser")
    soup.find("section", {"class": "default-content"})
    list = [span.text for span in soup.findAll("span", {"class": "luna-example italic"})]
    if list != []:
        usage_list = list[:2]
        usage_list.insert(0, "Usage in a Sentence:")
        return usage_list
    else:
        return [term, " does not have ", "a usage in a sentence."]
