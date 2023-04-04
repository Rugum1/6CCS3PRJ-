from pandarallel import pandarallel
from rank_bm25 import BM25Plus 
from ast import literal_eval
import pandas as pd
import pickle
import spacy
import csv

class BM25Creator: 

    def __init__(self,nlp):
        self.nlp = nlp 

    def create_model(self,corpus_file,output_file,model_name):
       df = pd.read_csv(corpus_file)
       pandarallel.initialize(progress_bar=True)
       df["tokenized_data"] =  df.paragraph.parallel_apply(self.tokenize_text)
       df.to_csv(output_file)

       tokenized_corpus = self.convert_dataframe_to_list(output_file)
       
       bm25 = BM25Plus(tokenized_corpus)
  
       self.save_BM25_model(model_name,bm25)
    
    """This method converts the pandas dataframe in a list of tokens that are needed 
       for the creation of the BM25 model"""
    def convert_dataframe_to_list(self,output_file):

        tokenized_corpus = []
  
        
        df = pd.read_csv("./" + output_file)
       
        for index in range(0,len(df)):
            tokenized_corpus.append(literal_eval(df.iloc[index]["tokenized_data"]))
        
        return tokenized_corpus
    
    """This method tokenizes the corpus by using a spacy model.The entities that are part of the NER model are not 
        going to be tokenized  """
    def tokenize_text(self,row): 
        
        raw_doc = self.nlp(row)
        doc = self.nlp(self.pre_process(raw_doc))
        word_list = []

        for i in range(0,len(doc)): 
            j = i
            if i < len(doc):
                if doc[j].ent_iob_ == "B":

                    while j<len(doc) and doc[j].ent_iob_ != "O": 

                        j+= 1 

                    word_list.append(doc[i:j].lemma_.strip())
                    i = j 
                elif doc[i].ent_iob_ != "I": 
                    if not doc[i].is_stop:
                        word_list.append(doc[i].lemma_.strip())
        
        return word_list
    
    def pre_process(self,doc): 
        processed_paragraph = ""
        for tok in doc: 
            if not tok.is_punct:
                cleaned_word = "".join(c for c in tok.lemma_ if c.isalpha())
                processed_paragraph += " " + cleaned_word.lower().strip()
        
        return processed_paragraph.strip()
    
    def save_BM25_model(self,file_name,bm25):
        with open(file_name, 'wb') as file:
            pickle.dump(bm25, file)
