import pickle
from rank_bm25 import BM25L
import pandas as pd
import spacy
from transformers import BertForQuestionAnswering
from transformers import AutoTokenizer
from transformers import pipeline
from pandarallel import pandarallel


df = pd.read_csv("./data2/concatenated_data_2.csv")

file_name = "BM25/model8(BM25+).pkl"
# load  model
with open(file_name, 'rb') as file:
    model = pickle.load(file)


query = "user interface"
nlp = spacy.load("en_core_web_sm")
doc = nlp(query)


tokenized_query = []
for tok in doc:
    word = tok.lemma_
    word = word.lower()
    print(word)
    tokenized_query.append(word)
    print(tokenized_query)



corpus = []
for index in range(0,len(df)):
    corpus.append(df.iloc[index]["paragraph"])

answer_list = model.get_top_n(["abstract type","implement"], corpus, n=10)

for element in answer_list:
    print(element)
    print()





# context = ""
# for answer in answer_list:
#     context += answer


# model = BertForQuestionAnswering.from_pretrained('deepset/bert-base-cased-squad2')

# tokenizer = AutoTokenizer.from_pretrained('deepset/bert-base-cased-squad2')
# tokenizer.encode(query,truncation = True, padding=True)

# nlp2 = pipeline('question-answering', model = model, tokenizer = tokenizer)


# print(nlp2({ 'question' : "What is an accesor method?",'context' : context}))
