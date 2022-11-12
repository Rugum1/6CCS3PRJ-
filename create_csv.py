
from data_processing.data_cleaner import DataCleaner
from data_processing.data_scraper import DataScraper
import csv
from NER_models.custom_ner_creator import NERCreator
import spacy
import json
from spacy.lang.en import English
from spacy.pipeline import EntityRuler

# url = "https://en.wikipedia.org/wiki/Glossary_of_computer_science#instruction"
# file = "./data/computer_science_glossary.json"
# scraper = DataScraper(url)
# sources = scraper.get_specific_tags("dfn")
#
# scraper.write_to_json_file_key_value_pair(file,sources)



# header = ["name","description"]
# scraper.write_to_csv_file(file,sources,header)


# with open("./data/computer_science_glossary.csv") as file_obj:
#
#     # Create reader object by passing the file
#     # object to DictReader method
#     reader_obj = csv.DictReader(file_obj)
#
#     # Iterate over each row in the csv file
#     # using reader object
#     x= 0
#     for row in reader_obj:
#         x = x + 1
#         print(row["name"])
#         print()
#     print(x)


# nlp = spacy.load("NER_models/abreviation_ner")
# doc = nlp("My bike is OOP")
#
# if len(doc.ents) >  0 :
#     print(doc.ents)
