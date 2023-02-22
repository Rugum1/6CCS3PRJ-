from transformers import BertForQuestionAnswering
from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter
from transformers import AutoTokenizer
from transformers import pipeline
import helpers as helpers 
import spacy

class CSTermsAdapter(LogicAdapter):

    
    model = BertForQuestionAnswering.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
    tokenizer = AutoTokenizer.from_pretrained('deepset/bert-large-uncased-whole-word-masking-squad2')
    bm25_model = helpers.load_bm25_model("BM25/model7(lematized).pkl")
    corpus = helpers.load_corpus("data/concatenated_data.csv")



    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)


    def can_process(self, statement):
        nlp = spacy.load("NER_models/cs_ner_5(lematized)")
        doc = nlp(statement.text)
        if len(doc.ents)  > 0:
            return True
        return False

    def process(self, input_statement, additional_response_selection_parameters):
        confidence = 1
        
        selected_statement = Statement(text = self.get_answer(input_statement.text))

        selected_statement.confidence = confidence

        return selected_statement
    

    def get_answer(self,query):


            tokenized_query = helpers.tokenize_text(query)

            context = self.get_context(tokenized_query)
          

            nlp2 = pipeline('question-answering', model = self.model, tokenizer = self.tokenizer)

            return nlp2({ 'question' : query ,'context' : context}).get("answer")


    def get_context(self,tokenized_query):

        combined_paragraphs =""
        answer_list = self.bm25_model.get_top_n(tokenized_query,self.corpus,n=10)

        for answer in answer_list:
            combined_paragraphs += "\n" + answer
            
        return combined_paragraphs
    

   
 

