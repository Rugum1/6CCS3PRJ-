from rank_bm25 import BM25Okapi
import csv
import spacy
import re
import pandas as pd
from pandarallel import pandarallel
from rank_bm25 import BM25L
from ast import literal_eval
import pickle



f1= "./data2/computer_science_index.csv"

def split_word(row):

    word_list = []
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(row)

    for token in doc:
        if len(token.text) > 2 and not token.is_punct  and not token.is_stop and not "/" in token.text and "*" not in token.text:
            if "\\" not in token.text and "^" not in token.text:
                pattern = '\.[0-9]+|\:[0-9]+|;.*|\,[0-9]+|^"|".*$|%.*$|&.*$|'

                word = token.lemma_
                word = re.sub(pattern,"",word)
                word = word.lower()

                if len(word) > 0:
                    word_list.append(word)

    return word_list



df = pd.read_csv(f1)

pandarallel.initialize(progress_bar=True)

df["split_paragraph"] = df.paragraph.parallel_apply(split_word)

# df.drop(columns=['number'], inplace=True)
df.to_csv('data2/processed_computer_science_index.csv')

df2 = pd.read_csv('data2/processed_computer_science_index.csv')

tokenized_corpus = []
corpus = []

for index in range(0,len(df2)):
    tokenized_corpus.append(literal_eval(df2.iloc[index]["split_paragraph"]))
    corpus.append(df2.iloc[index]["paragraph"])

bm25 = BM25L(tokenized_corpus)

# save model
file_name = "BM25/model2.pkl"
with open(file_name, 'wb') as file:
    pickle.dump(bm25, file)
