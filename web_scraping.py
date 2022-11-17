import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


xPath ="//dfn[contains(@class, 'glossary')]/a"

driver = webdriver.Safari()
driver.get("https://en.wikipedia.org/wiki/Glossary_of_computer_science")
all_options = driver.find_elements(By.XPATH, xPath)

link_list = []

for option in all_options:
    link_list.append(option.get_attribute("href"))


paragraph_list = []
xPath2 =  "//p"
for i in range(2) :
    print(link_list[i])
    driver.get(link_list[i])
    all_paragraphs = driver.find_elements(By.XPATH, xPath2)
    for paragraph in all_paragraphs:
        paragraph_list.append(paragraph.text)

file = "./data/computer_science_dataset.json"
j = 0
with open(file,'w',encoding = "utf-8") as f:
    for paragraph in paragraph_list:
        f.write(json.dumps({j:paragraph })+ ",\\n")
        j+= 1


print(len(paragraph_list))
print(len(all_options))
