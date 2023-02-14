from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import spacy
from  spell_checker import CSTermsSpellChecker
from database_functions import DbFunctions
from answer_processor import AnswerProcessor

class CSTermsAdapter(LogicAdapter):

    answer_processor = AnswerProcessor()


    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)


    def can_process(self, statement):
        spell = CSTermsSpellChecker()
        nlp = spacy.load("NER_models/cs_ner_5(lemmatized)")
        doc = nlp(statement.text)
        if len(doc.ents)  > 0:
            return True
        return False

    def process(self, input_statement, additional_response_selection_parameters):
        confidence = 1

        nlp = spacy.load("NER_models/cs_ner_3")
        doc = nlp(input_statement.text)
        ent = doc.ents
       
        selected_statement = Statement(text = self.answer_processor.get_answer(input_statement.text))

        selected_statement.confidence = confidence

        return selected_statement
