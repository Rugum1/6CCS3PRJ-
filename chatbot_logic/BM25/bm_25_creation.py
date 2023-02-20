from rank_bm25 import BM25Okapi
import csv
import spacy
import re
import pandas as pd
from pandarallel import pandarallel
from rank_bm25 import BM25Plus
from ast import literal_eval
import pickle


nlp = spacy.load("en_core_web_sm")
nlp.remove_pipe("ner")
nlp.add_pipe("entity_ruler", source=spacy.load("./NER_models/cs_ner_5(lematized)"))
nlp.add_pipe('sentencizer')



f1= "./data2/concatenated_data_2.csv"


def pre_process(doc): 
    processed_paragraph = ""
    for tok in doc: 
        if not tok.is_punct:
            cleaned_word = "".join(c for c in tok.lemma_ if c.isalpha())
            processed_paragraph += " " + cleaned_word.lower().strip()
    
    return processed_paragraph.strip()



def tokenize_text(row): 
    
    raw_doc = nlp(row)
    doc = nlp(pre_process(raw_doc))
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



df = pd.read_csv(f1)

pandarallel.initialize(progress_bar=True)


df["split_paragraph"] = df.paragraph.parallel_apply(tokenize_text)

df.drop(columns=['number'], inplace=True)
df.to_csv('data2/processed_concatenated_data.csv')

df2 = pd.read_csv('data2/processed_concatenated_data.csv')

tokenized_corpus = []
corpus = []

for index in range(0,len(df2)):
    tokenized_corpus.append(literal_eval(df2.iloc[index]["split_paragraph"]))
    corpus.append(df2.iloc[index]["paragraph"])

bm25 = BM25Plus(tokenized_corpus)

# save model
file_name = "BM25/model8(BM25+).pkl"
with open(file_name, 'wb') as file:
    pickle.dump(bm25, file)
