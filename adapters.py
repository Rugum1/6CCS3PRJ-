from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import spacy
from helper_methods_for_adapters import CsTermsAdapterHelpers
from  spell_checker import CSTermsSpellChecker
from database_functions import DbFunctions

class CSTermsAdapter(LogicAdapter):


    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)


    def can_process(self, statement):
        spell = CSTermsSpellChecker()
        text_input = spell.check_spelling(statement.text)
        nlp = spacy.load("NER_models/cs_ner")
        doc = nlp(text_input)
        for ent in doc.ents:
            if ent.label_  == "CS_TERM":
                return True
        return False

    def process(self, input_statement, additional_response_selection_parameters):
        confidence = 1

        nlp = spacy.load("NER_models/cs_ner")
        doc = nlp(input_statement.text)
        ent = doc.ents
        db = DbFunctions()

        sql = "SELECT DESCRIPTION FROM CS_TERM WHERE name=?"


        response = db.select_term_from_db(sql,ent[0].text)


        selected_statement = Statement(text = response)


        selected_statement.confidence = confidence


        return selected_statement

class CSAbreviationAdapter(LogicAdapter):


    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)


    def can_process(self, statement):
        spell = CSTermsSpellChecker()
        text_input = spell.check_spelling(statement.text)
        nlp = spacy.load("NER_models/abreviation_ner")
        doc = nlp(statement.text)
        for ent in doc.ents:
            if ent.label_  == "CS_ABREVIATION":
                return True
        return False

    def process(self, input_statement, additional_response_selection_parameters):
        confidence = 1

        nlp = spacy.load("NER_models/abreviation_ner")
        doc = nlp(input_statement.text)
        ent = doc.ents
        db = DbFunctions()

        sql = "SELECT DESCRIPTION FROM CS_ABREVIATION WHERE name=?"

        response = db.select_term_from_db(sql,ent[0].text)

        selected_statement = Statement(text = response)

        selected_statement.confidence = confidence

        return selected_statement
