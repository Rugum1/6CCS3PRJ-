import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from top2vec import Top2Vec


xPath ="//dfn[contains(@class, 'glossary')]/a"

driver = webdriver.Safari()
driver.get("https://en.wikipedia.org/wiki/Glossary_of_computer_science")
all_options = driver.find_elements(By.XPATH, xPath)

link_list = []

for option in all_options:
    link_list.append(option.get_attribute("href"))


paragraph_list = []
xPath2 =  "//p"
for link in link_list:
    driver.get(link)
    all_paragraphs = driver.find_elements(By.XPATH, xPath2)
    for paragraph in all_paragraphs:
        print(paragraph.text)
        print()
        paragraph_list.append(paragraph.text)

file = "./data/computer_science_dataset.csv"
j = 0
header=["number","paragraph"]
with open(file,'w',encoding ="utf-8", newline ='') as f:
     writer = csv.writer(f)
     writer.writerow(header)
     for paragraph in paragraph_list:
         paragraph=paragraph.strip()
         paragraph=paragraph.replace("(","").replace(")","").replace("{","").replace("}","")
         paragraph = paragraph.replace("[","").replace("]","")
         paragraph = ' '.join(paragraph.split())
         if paragraph != "" and len(paragraph.split()) > 5:
              writer.writerow([j,paragraph])
              j+= 1



print(len(paragraph_list))
print(len(all_options))
