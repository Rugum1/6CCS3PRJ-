from transformers import BertForQuestionAnswering
from transformers import AutoTokenizer
from transformers import pipeline
import pandas as pd
import pickle


def load_bm25_model(file_name):
    with open(file_name, 'rb') as file:
        model = pickle.load(file)
    return model


def load_corpus(file_name):
    df = pd.read_csv(file_name)
    corpus = df['paragraph'].astype(str).values.tolist()
    return corpus

def get_answer(query):
    model = BertForQuestionAnswering.from_pretrained('deepset/bert-base-cased-squad2')
    tokenizer = AutoTokenizer.from_pretrained('deepset/bert-base-cased-squad2')
    tokenizer.encode(query,truncation = True, padding=True)
    
    nlp = pipeline('question-answering', model = model, tokenizer = tokenizer)

    return nlp2({ 'question' : "What is an accesor method?",'context' : context})
