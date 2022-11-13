
from data_processing.data_cleaner import DataCleaner
from data_processing.data_scraper import DataScraper
import csv
from NER_models.custom_ner_creator import NERCreator
import spacy
import json
from spacy.lang.en import English
from spacy.pipeline import EntityRuler
from database_functions import DbFunctions

# url = "https://www.oracle.com/java/technologies/glossary.html"
#
file = "./data/java_glossary.csv"
# scraper = DataScraper(url)
# sources = scraper.get_specific_tags("strong")
# #

# for source in sources:
#     text = source.get_text().strip()
#     if len(text) == 1 :
#         print(source.get_text())
# scraper.write_to_json_file(file,sources)
db = DbFunctions()



sql ='''CREATE TABLE JAVA_TERM(
   NAME CHAR(100) NOT NULL,
   DESCRIPTION VARCHAR NOT NULL
)'''
db.create_new_table(sql)
#
# #
db.insert_elements_in_database("JAVA_TERM",file)



# header = ["name","description"]
# scraper.write_to_csv_file(file,sources,header)



# f = "./data/computer_science_.csv"
# out = "./data/computer_science_glossary_v2.csv"
#
# data = []
# with open(file,'r') as file_obj:
#
#     # Create reader object by passing the file
#     # object to DictReader method
#     reader_obj = csv.DictReader(file_obj)
#
#
#     for row in reader_obj:
#         data.append(row["name"])


# scraper = DataScraper("none")
#
# scraper.write_to_json_file("./data/java_glossary.json",data)

# nlp = spacy.load("NER_models/abreviation_ner")
# doc = nlp("My bike is OOP")
#
# if len(doc.ents) >  0 :
#     print(doc.ents)
#
# file_dict = {"./data/computer_science_glossary.json" : "CS_TERM", "./data/computer_science_abreviations.json" : "CS_ABREVIATION","./data/java_glossary.json" : "JAVA_TERM"}
#
# ner = NERCreator(file_dict,"cs_ner_2")
#
# ner.create_custom_NER_model()
