
import pandas as pd
import NER_models
from NER_models import custom_ner_creator


f1 = "./data2/computer_science_index.csv"
f2 = "./data/computer_science_dataset.csv"
f3 = "./data/computer_science_glossary.csv"


df1 = pd.read_csv(f1)
df2 = pd.read_csv(f2)

df2.drop(columns=['number'], inplace=True)


df_concat = pd.concat([df1,df2],ignore_index=True)



df_concat.to_csv('data2/concatenated_data_2.csv')