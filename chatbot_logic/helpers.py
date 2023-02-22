from transformers import BertForQuestionAnswering
from transformers import AutoTokenizer
from transformers import pipeline
import pandas as pd
import pickle
import spacy 


def load_bm25_model(file_name):
    with open(file_name, 'rb') as file:
        model = pickle.load(file)
    return model


def load_corpus(file_name):
    df = pd.read_csv(file_name)
    corpus = df['paragraph'].astype(str).values.tolist()
    return corpus


def load_nlp(): 

    nlp = spacy.load("en_core_web_sm")
    nlp.remove_pipe("ner")
    nlp.add_pipe("entity_ruler", source=spacy.load("./NER_models/cs_ner_5(lematized)"))
    nlp.add_pipe('sentencizer')
    
    return nlp 

def pre_process(doc): 
    processed_paragraph = ""
    for tok in doc: 
        if not tok.is_punct:
            cleaned_word = "".join(c for c in tok.lemma_ if c.isalpha())
            processed_paragraph += " " + cleaned_word.lower().strip()
    
    return processed_paragraph.strip()


def tokenize_text(text): 
    
    nlp = load_nlp()
    raw_doc = nlp(text)
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


def get_context_without_tokenized_query(query): 
        
        model = load_bm25_model("BM25/model7(lematized).pkl")

        combined_paragraphs =""
        
        tokenized_query = tokenize_text(query)

        answer_list = model.get_top_n(tokenized_query,load_corpus("data2/concatenated_data_2.csv"),n=10)
    
        for answer in answer_list:
           combined_paragraphs += "\n" + answer
        
        return combined_paragraphs

