# Scraping from wikipedia page:

import requests as req
from bs4 import BeautifulSoup as bs


def results(url):
    response = req.get(url)
    soup = bs(response.content,'html.parser' )
    result = soup.find_all(class_="noprint Inline-Template Template-Fact")
    return result


def get_citations_needed_count(results):
    citation_count = len(results)
    return citation_count

def get_citations_needed_report(results):
    report = []
    for citation in results:
        text = citation.find_parent().text
        report.append(text)
    return "\n\n".join(report)

if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/UNESCO_Institute_for_Statistics'
    result_info = results(url)
    count = get_citations_needed_count(result_info)
    print(f"Citation count: {count} \n")
    report = get_citations_needed_report(result_info)
    print(f"Citation report: {report}\n")