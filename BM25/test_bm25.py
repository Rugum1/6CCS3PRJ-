import pickle
from rank_bm25 import BM25L
import pandas as pd
import spacy
from transformers import BertForQuestionAnswering
from transformers import AutoTokenizer
from transformers import pipeline


df = pd.read_csv("./data2/whole_page_indexed.csv")

file_name = "BM25/model3.pkl"
# load  model
with open(file_name, 'rb') as file:
    model = pickle.load(file)


query = "scope"
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

answer_list = model.get_top_n(tokenized_query, corpus, n=1)

print(answer_list[0])

# for element in answer_list:
#     print(element)
#     print()


context = ""
for answer in answer_list:
    context += answer


model = BertForQuestionAnswering.from_pretrained("deepset/bert-large-uncased-whole-word-masking-squad2")

tokenizer = AutoTokenizer.from_pretrained('deepset/bert-large-uncased-whole-word-masking-squad2')

nlp2 = pipeline('question-answering', model = model, tokenizer = tokenizer)


print(nlp2({ 'question' : "what is scope?",'context' : answer_list[0]}))
