import pandas as pd
from top2vec import Top2Vec
import spacy
from spacy.matcher import PhraseMatcher
import PyPDF2



df = pd.read_csv(r'data/computer_science_dataset.csv')
docs = df.paragraph.tolist()

model = Top2Vec.load("top_vec")

pdfFileObj = open('ObjectFirst.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)
