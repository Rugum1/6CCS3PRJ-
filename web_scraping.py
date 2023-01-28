import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from top2vec import Top2Vec
from transformers import pipeline
import pandas as pd


summarizer = pipeline("summarization", model="philschmid/bart-large-cnn-samsum")

xPath ="//div[contains(@style, 'width:46%; float:left; margin:0; padding:10px;')]//ul//li//a"
# "//div[contains(@class, 'mw-content-container')]/a"

driver = webdriver.Safari()
driver.get("https://en.wikipedia.org/wiki/Index_of_object-oriented_programming_articles")
all_options = driver.find_elements(By.XPATH, xPath)
df2 = pd.read_csv("./data2/links.csv")

# link_list = []
# i = 0
# for option in all_options:
#
#     if i < 20:
#         link_list.append(option.get_attribute("href"))
#         i+=1
#

paragraph_list = []
xPath2 =  "//a"
xPath3 = "//span[@class= 'mw-headline']/following-sibling::*"
for i in range(len(df2)):
    driver.get(df2.iloc[i]["link"])
    all_paragraphs = driver.find_elements(By.XPATH, xPath2)
    article = ""
    combined_paragraphs =""
    for paragraph in all_paragraphs:
        paragraph_list.append(paragraph.text)


file = "./data2/object_oriented_terms.csv"
j = 0
header=["paragraph"]
with open(file,'w',encoding ="utf-8", newline ='') as f:
     writer = csv.writer(f)
     writer.writerow(header)
     for paragraph in paragraph_list:
        #  print(paragraph)
        #  paragraph=paragraph.strip()
        #  paragraph=paragraph.replace("(","").replace(")","").replace("{","").replace("}","")
        #  paragraph = paragraph.replace("[","").replace("]","")
        #  paragraph = ' '.join(paragraph.split())
        #  if paragraph != "" and len(paragraph.split()) > 5:
        writer.writerow([paragraph])






print(len(paragraph_list))
print(len(all_options))
