from gensim.models.word2vec import Word2Vec
from gensim.models.keyedvectors import KeyedVectors
import pandas as pd
import multiprocessing
import spacy
import re
import json
df = pd.read_csv(r'data/computer_science_dataset.csv')

def pre_process_data(file):
    docs = df.paragraph.tolist()
    nlp = spacy.load("en_core_web_lg")
    processed_list = []
    stop_words = nlp.Defaults.stop_words
    all_sent_list = []
    for paragraph in docs:
        doc = nlp(paragraph)
        for sent in doc.sents:
             sent_word_list = []
             sent = re.sub(r'[^\w\s]', '', sent.text)
             sent = re.sub(r'http\S+', '', sent)
             sent = re.sub(r'[0-9]', '', sent)
             list_of_words = sent.split(" ")
             for word in list_of_words:
                 if word not in stop_words:
                     if len(word) in range(3,30):
                         sent_word_list.append(word.lower())
             all_sent_list.append(sent_word_list)
    wirite_data_to_json(file,all_sent_list)


def wirite_data_to_json(file,list):
    with open(file,'w',encoding = "utf-8") as f:
        json.dump(list,f,indent=4)

def load_data(file):
    with open(file,'r',encoding = "utf-8") as f:
        data = json.load(f)

    return data



def create_word_vec():
    data = load_data("data/word_vec_data.json")
    cores = multiprocessing.cpu_count()
    word_vec_model = Word2Vec(min_count=5,
                              window=2,
                              vector_size=500,
                              sample=6e-5,
                              alpha=0.33,
                              min_alpha=0.0007,
                              negative=20,
                              workers=cores-1)
    word_vec_model.build_vocab(data)
    word_vec_model.train(data,total_examples=word_vec_model.corpus_count,epochs=30)
    word_vec_model.wv.save_word2vec_format(f"word_vec/word2vec_cs_model.txt")
