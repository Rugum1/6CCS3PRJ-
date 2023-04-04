import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from top2vec import Top2Vec
from transformers import pipeline
import pandas as pd


class WebScraper(): 

    def __init__(self,links_file,output_file,xPath):

        self.scrape_data(links_file,output_file)

    
    def scrape_data(self, links_file,output_file,xPath): 

        driver = webdriver.Safari()
        df2 = pd.read_csv(links_file)
        paragraph_list = ''

        for i in range(len(df2)):
            driver.get(df2.iloc[i]["link"])
            all_paragraphs = driver.find_elements(By.XPATH, xPath)
            article = ""
            combined_paragraphs =""
            for paragraph in all_paragraphs:
                paragraph_list.append(paragraph.text)
        
        self.save_data(paragraph_list,output_file)
    


    def save_data(self,paragraph_list, output_file):
        
        header=["paragraph"]
        with open(output_file,'w',encoding ="utf-8", newline ='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for paragraph in paragraph_list:
                writer.writerow([paragraph])
        
        print("Data has been saved")


            






      




