import spacy
import pandas as pd
from chatbot import ChatBotStudentAid
from NER_models.custom_ner_creator import NERCreator
import time

df = pd.read_csv("data/experiment_data.csv")
nlp = spacy.load("en_core_web_lg") 
accumulator = 0

bot = ChatBotStudentAid()
dict = {} 
for index, row in df.iterrows():

    question = "What is " + row["name"] + "?"
    answer = bot.get_answer(question)
    time.sleep(1)

    doc1 = nlp(answer.text)
    doc2 = nlp(row["description"])
    print(index)

    if doc1.similarity(doc2) <= 0.5 : 
        dict.update({question :answer.text })

    accumulator = accumulator + doc1.similarity(doc2)

print(accumulator/df.size)


    
   




   


