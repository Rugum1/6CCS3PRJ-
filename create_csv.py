
from data_processing.data_cleaner import DataCleaner
from data_processing.data_scraper import DataScraper
import csv
from NER_models.custom_ner_creator import NERCreator
import spacy
import json
from spacy.lang.en import English
from spacy.pipeline import EntityRuler
from database_functions import DbFunctions

# url = "https://en.wikipedia.org/wiki/List_of_computing_and_IT_abbreviations"
#
file = "./data/computer_science_abreviations.csv"
# scraper = DataScraper(url)
# sources = scraper.get_specific_tags("li")
# #

# scraper.write_to_json_file(file,sources)
# db = DbFunctions()
#
#
#
# sql ='''CREATE TABLE CS_ABREVIATION(
#    NAME CHAR(100) NOT NULL,
#    DESCRIPTION VARCHAR NOT NULL
# )'''
# db.create_new_table(sql)
#
# #
# db.insert_elements_in_database("CS_ABREVIATION",file)



# header = ["name","description"]
# scraper.write_to_csv_file_v2(file,sources,header)



# f = "./data/computer_science_.csv"
# out = "./data/computer_science_glossary_v2.csv"
#
with open(file,'r') as file_obj:

    # Create reader object by passing the file
    # object to DictReader method
    reader_obj = csv.DictReader(file_obj)


    for row in reader_obj:
        if row["name"] in (None, ""):
            print(row["description"])



# nlp = spacy.load("NER_models/abreviation_ner")
# doc = nlp("My bike is OOP")
#
# if len(doc.ents) >  0 :
#     print(doc.ents)
