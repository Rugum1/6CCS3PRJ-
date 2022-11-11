from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import spacy
from helper_methods_for_adapters import CsTermsAdapterHelpers
import wikipedia
from  spell_checker import CSTermsSpellChecker as spell

class CsTermsAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)


    def can_process(self, statement):
        statement.text = spell.check_spelling(statement.text)
        text_input = statement.text
        nlp = spacy.load("cs_ner")
        doc = nlp(text_input)
        for ent in doc.ents:
            if ent.label_  == "CS_TERM":
                return True
        return False

    def process(self, input_statement, additional_response_selection_parameters):
        
        confidence = 1

        nlp = spacy.load("cs_ner")
        doc = nlp(input_statement.text)
        ent = doc.ents

        response = CsTermsAdapterHelpers.get_sources(ent[0].text)

        selected_statement = Statement(text = response)

        selected_statement.confidence = confidence

        return selected_statement
