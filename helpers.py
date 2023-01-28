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
