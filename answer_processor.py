from transformers import BertForQuestionAnswering
from transformers import AutoTokenizer
from transformers import pipeline
import helpers
import spacy

class AnswerProcessor():

    model = BertForQuestionAnswering.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
    tokenizer = AutoTokenizer.from_pretrained('deepset/bert-large-uncased-whole-word-masking-squad2')
    bm25_model = helpers.load_bm25_model("BM25/model7(lematized).pkl")
    corpus = helpers.load_corpus("./data2/concatenated_data_2.csv")


    def get_answer(self,query):


        tokenized_query = helpers.tokenize_text(query)

        context = self.get_context(tokenized_query)
        print(context)

        nlp2 = pipeline('question-answering', model = self.model, tokenizer = self.tokenizer)

        return nlp2({ 'question' : query ,'context' : context})


    def get_context(self,tokenized_query):

        combined_paragraphs =""
        answer_list = self.bm25_model.get_top_n(tokenized_query,self.corpus,n=10)

        for answer in answer_list:
            combined_paragraphs += "\n" + answer
            
        return combined_paragraphs
