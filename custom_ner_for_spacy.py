import spacy
import json
from spacy.lang.en import English
from spacy.pipeline import EntityRuler


def load_data(file):
    with open(file , "r", encoding ="utf-8") as f:
        data = json.load(f)
    return(data)


def clean_up_data(file):
    clean_data = []
    data = load_data(file)
    abreviation_data = load_data("./data/computer_science_abreviations.json")
    # print_data(abreviation_data)
    # clean_data = remove_special_charachters(data)
    # clean_data = remove_abreviations(abreviation_data,data)
    add_new_processed_data_to_document(abreviation_data,data,file)

def remove_special_charachters(data):
    clean_data = []
    for cs_term in data:
        cs_term = cs_term.replace("(", "").replace(")", "").replace("-", " ").replace(",", " ")
        if cs_term not in data:
            clean_data.append(cs_term)
    return clean_data

def remove_abreviations(abreviation_data,data):
    clean_data = []
    for cs_abreviation in abreviation_data:
        for cs_term in data:
            if "(" not in cs_term:
               cs_term = cs_term.replace(cs_abreviation,"")
               if cs_term not in data:
                clean_data.append(cs_term)
    print_data(clean_data)

def print_data(data):
    for cs_term in data:
        print(cs_term)

def add_new_processed_data_to_document(clean_data,data,file):
    data = append_new_cleaned_data(clean_data,data)
    with open(file,'w',encoding = "utf-8") as f:
        for cs_term in data:
            f.write(json.dumps(cs_term) + ",\n")

def append_new_cleaned_data(clean_data,data):
    for cs_term in clean_data:
        data.append(cs_term)
    return data


#This method was taken from Python tutorials for digital humanities
def create_training_data(file,type):
    data = load_data("./data/computer_science_glossary.json")
    patterns = []
    for cs_term in data:
        pattern = {
                    "label" : type,
                    "pattern" : cs_term
                  }
        patterns.append(pattern)
    return (patterns)

#This method was taken from Python tutorials for digital humanities
def generate_rules(patterns):
    nlp = English()
    ruler = nlp.add_pipe("entity_ruler")
    ruler.add_patterns(patterns)
    nlp.to_disk("cs_ner")
