from transformers import pipeline
import pandas as pd
from pandarallel import pandarallel




summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
f1= "./data/computer_science_dataset.csv"

summary_list = []

def create_summary(row):
    paragraph = row
    paragraph_length = len(paragraph.split())
    summary = summarizer(paragraph, max_length=int(paragraph_length), min_length=int(paragraph_length/2), do_sample=False)


    return summary

df = pd.read_csv(f1)

pandarallel.initialize(progress_bar=True)

df["paragraph_summary"] = df.paragraph.parallel_apply(create_summary)
df.drop(columns=['number'], inplace=True)
df.to_csv('data/summarized_cs_data.csv')
