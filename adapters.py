from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
from bs4 import BeautifulSoup
import wikipedia
import requests
import spacy
import difflib
from difflib import SequenceMatcher

class MyLogicAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)


    def can_process(self, statement):
        # nlp = spacy.load("cs_ner")
        # doc = nlp(statement.text)
        # for ent in doc.ents:
        #     if ent.label_ is "CS_TERM":
        #         return True
        return True


    def create_serach_id(term):
        list_of_words = term.split()
        id = ""
        for i  in len(list_of_words):
            if i < len(list_of_words) - 1 :
                 id+= list_of_words.get(i) + "_"

        return id



    def process(self, input_statement, additional_response_selection_parameters):
        confidence = 1

        nlp = spacy.load("cs_ner")
        doc = nlp(input_statement.text)
        ent = doc.ents

        url = "https://en.wikipedia.org/wiki/Glossary_of_computer_science"

        s = requests.get(url)
        soup = BeautifulSoup(s.text,"lxml")

        query = ent[0].text.replace(" ", "_")

        print(query)
        sources = soup.find("dt",{"id": query})
        print(sources)


        response = sources.findNext("dd").get_text()


        selected_statement = Statement(text = response)

        selected_statement.confidence = confidence

        return selected_statement
