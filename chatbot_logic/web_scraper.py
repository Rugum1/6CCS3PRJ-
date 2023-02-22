from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import csv


class Web_Scraper(): 

    

    def scrape_data(self,url_file,output_file,xPath): 

        driver = webdriver.Safari()
        df = pd.read_csv(url_file)
        paragraph_list = []

        for i in range(len(df)):
            driver.get(df.iloc[i]["link"])
            all_paragraphs = driver.find_elements(By.XPATH, xPath)
            article = ""
            combined_paragraphs =""
            for paragraph in all_paragraphs:
                paragraph_list.append(paragraph.text)
        
        self.save_file(output_file)

        print("All paragraphs scraped")
        

    
    def save_file(self,file,paragraph_list): 

        header=["paragraph"]

        with open(file,'w',encoding ="utf-8", newline ='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for paragraph in paragraph_list:
                writer.writerow([paragraph])



        





    