import requests
from bs4 import BeautifulSoup

term = "a"

def presuf(term):
    term = term
    response = requests.get("https://www.dailywritingtips.com/list-prefixes-suffixes/")
    soup = BeautifulSoup(response.text, "html.parser")
    soup.find("section", {"class": "post"})
    list = [span.text for span in soup.findAll("p", {"scrollHeight": 1840})]

    print(list)

presuf(term)