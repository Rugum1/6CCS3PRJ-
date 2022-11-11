import requests
from bs4 import BeautifulSoup

class GeneralHelper():

    def load_page_url(url):
        try:
            s = requests.get(url)
            return s
        except requests.exceptions.RequestException as e:
            print("We could not load the answer to your questions.")
            raise SystemExit(e)

class CsTermsAdapterHelpers():

    def get_sources(query):
        query.replace(' ','_')
        s = GeneralHelper.load_page_url("https://en.wikipedia.org/wiki/Glossary_of_computer_science")
        soup = BeautifulSoup(s.text,"lxml")
        sources = soup.find("dt",{"id": query})

        if sources is not None:
            return sources.findNext("dd").get_text()
        else:
            return "The answer could not be retrieved"
