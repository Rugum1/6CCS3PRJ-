from bs4 import BeautifulSoup
import requests
import json
import csv
from .data_cleaner import DataCleaner
class DataScraper:

    url  = None

    def __init__(self,url):
        self.url = url

    def get_specific_tags(self,tag):
        s = requests.get(self.url)
        soup = BeautifulSoup(s.text,"lxml")
        sources = soup.findAll(tag)
        return sources

    def get_specific_tags_based_on_class(self,tag,tag_class):
        s = requests.get(self.url)
        soup = BeautifulSoup(s.text,"lxml")
        sources = soup.findAll(tag, {"class": tag_class})
        return sources

    def get_next_tag(self,source,tag):
        return source.findNext(tag)

    def write_to_json_file(self,file,data):
        with open(file,'w',encoding = "utf-8") as f:
            for input_text in data:
                f.write(json.dumps(input_text) + ",\n")


    def write_to_csv_file_v2(self,file,sources,header):
         with open(file,'w',encoding ="utf-8", newline ='') as f:
             writer = csv.writer(f)
             writer.writerow(header)
             for source in sources:
                 writer.writerow([source.findNext("a").get_text(),source.get_text().replace(",","")])


    def write_to_json_file_v2(self,file,sources):
         with open(file,'w',encoding = "utf-8") as f:
             cleaner = DataCleaner()
             for source in sources:
                 f.write(json.dumps(source.get_text()) + ",\n")
                 if "-" in source.get_text():
                     f.write(json.dumps(source.get_text().replace("-"," ")) + ",\n")
                 if "(" in source.get_text():
                    f.write(json.dumps(source.get_text().replace("(","").replace(")","")) + ",\n" )

                    if "-" in source.get_text():
                        f.write(json.dumps(source.get_text().replace("(","").replace(")","").replace("-"," ")) + ",\n")

                        data = cleaner.remove_abreviations(source.get_text().replace("(","").replace(")",""))
                        f.write(json.dumps(data[0].strip()) + ",\n")

                    data = cleaner.remove_abreviations(source.get_text().replace("(","").replace(")","").replace("-"," "))
                    f.write(json.dumps(data[0].strip()) + ",\n")


    def write_to_csv_file(self,file,sources,header):
        with open(file,'w',encoding ="utf-8", newline ='') as f:
            cleaner = DataCleaner()
            writer = csv.writer(f)
            writer.writerow(header)
            for source in sources:
                text  = source.get_text().strip()
                if  len(text) > 1:
                    writer.writerow([source.get_text().strip(),source.findNext("p").get_text()])
                    if "-" in source.get_text():
                        writer.writerow([source.get_text().replace("-"," ").strip(),source.findNext("p").get_text()])


                    if "(" in source.get_text():
                        writer.writerow([source.get_text().replace("(","").replace(")","").strip(),source.findNext("p").get_text()])


                        if "-" in source.get_text():
                            writer.writerow([source.get_text().replace("(","").replace(")","").replace("-"," ").strip(), source.findNext("p").get_text()])

                            data = cleaner.remove_abreviations(source.get_text().replace("(","").replace(")",""))
                            writer.writerow([data[0].strip(), source.findNext("p").get_text()])

                        data = cleaner.remove_abreviations(source.get_text().replace("(","").replace(")","").replace("-"," ").strip())
                        writer.writerow([data[0].strip(), source.findNext("p").get_text()])
