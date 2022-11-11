
import wikipedia
from bs4 import BeautifulSoup
import requests
import json
from difflib import SequenceMatcher
import difflib
from operator import attrgetter
url = "https://en.wikipedia.org/wiki/Glossary_of_computer_science"

# print(SequenceMatcher(None, "abstract data type", "abstract data type(ADT)").ratio())
# print(SequenceMatcher(None))
# file = "./data/computer_science_abreviations.json"
#
# s = requests.get(url)
# soup = BeautifulSoup(s.text,"lxml")
# sources = soup.findAll("dt", {"class" : "glossary"})
# list_of_strings = []
#
# for source in sources:
#     if SequenceMatcher(None,source.get_text(),"abstract data type").ratio() > 0.7:
#         print(source.string)




    # if (SequenceMatcher(None, source.get_text(), "abstract data type").ratio() > 0.6):
    #     list_of_strings.append(source.get_text())
    #     print(source.get_text(),SequenceMatcher(None, source.get_text(), "abstract data type").ratio() )







# print(difflib.get_close_matches("abstract data type", list_of_strings))
#
# print(wikipedia.summary("abstract data type", sentences=3))
# for source in sources:
#     list_of_cs_terms.append(source.get_text())
#
# print(list_of_cs_terms)
# #
#
# with open(file,'w',encoding = "utf-8") as f:
#     for cs_term in list_of_cs_terms:
#         f.write(json.dumps(cs_term) + ",\n")
