from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Battle_of_the_Bulge"

page = requests.get(url)

print(page.content)

def get_citation_count():
    pass

def get_citation_report():
    pass

def get_citation_heading():
    pass
