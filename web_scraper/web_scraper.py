from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Coronavirus_disease_2019"


def get_citation_count():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    anchor_tags = soup.find_all('a')
    cite_count = 0

    for tag in anchor_tags:
        text = tag.get_text()
        if 'citation needed' in text:
            cite_count += 1

    print(cite_count)
    return(cite_count)

def get_citation_report():
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    anchor_tags = soup.find_all('a')

    report = ''

    for tag in anchor_tags:
        text = tag.get_text()
        if 'citation needed' in text:
            report += '*********CITATION*********** \n'
            report += f'{tag.parent.parent.parent.get_text()} \n'

    print(report)
    return report

def get_citation_heading():
    headings = []

    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    anchor_tags = soup.find_all("a")

    heading_tags = ['h1','h2','h3','h4','h5','h6']

    for tag in anchor_tags:

        text = tag.get_text()

        if "citation needed" in text:
            elem = tag.parent.parent.parent

            for prev_sib in elem.previous_siblings:
                if prev_sib.name in heading_tags:
                    headings.append(prev_sib.text)
                    break

    
    print(headings)
    return headings

get_citation_count()
get_citation_report()
get_citation_heading()