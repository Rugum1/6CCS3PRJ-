from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import spacy
from helper_methods_for_adapters import CsTermsAdapterHelpers
from  spell_checker import CSTermsSpellChecker
from database_functions import DbFunctions
import helpers

class CSTermsAdapter(LogicAdapter):

    model = helpers.load_bm25_model("BM25/model2.pkl")
    corpus = helpers.load_corpus("./data2/processed_computer_science_index.csv")


    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)


    def can_process(self, statement):
        spell = CSTermsSpellChecker()
        # text_input = spell.check_spelling(statement.text)
        nlp = spacy.load("NER_models/cs_ner_2")
        doc = nlp(statement.text)
        if len(doc.ents)  > 0:
            return True
        return False

    def process(self, input_statement, additional_response_selection_parameters):
        confidence = 1

        nlp = spacy.load("NER_models/cs_ner_2")
        doc = nlp(input_statement.text)
        ent = doc.ents
        db = DbFunctions()

        sql = "SELECT DESCRIPTION FROM " + ent[0].label_ + " WHERE name=?"

        response = db.select_term_from_db(sql,ent[0].text)

        selected_statement = Statement(text = response)

        selected_statement.confidence = confidence

        return selected_statement
