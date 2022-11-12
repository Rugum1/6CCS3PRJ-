import spacy
import json
import spacy
class DataCleaner:


    def load_data(self,file):
        with open(file , "r", encoding ="utf-8") as f:
            data = json.load(f)
        return(data)

    def remove_special_charachters(data,special_charchters):
        clean_data = []
        for term in data:
            for charachter in special_charchters:
                term = term.replace(special_charchters,"")
            if term not in data:
                clean_data.append(cs_term)
        return clean_data

    def remove_dashes(data):
        clean_data =[]
        for term in data:
            term = trem.replace("-"," ")
            clean_data.append(term)
        return clean_data

    def remove_abreviations(self,term):
        clean_data = []
        nlp = spacy.load("NER_models/abreviation_ner")
        doc = nlp(term)
        if len(doc.ents) > 0:
             ent = doc.ents
             term = term.replace(ent[0].text,"")
        clean_data.append(term)
        return(clean_data)

    def print_data(data):
        for term in data:
            print(term)

    def add_new_processed_data_to_document(data,file):
        with open(file,'w',encoding = "utf-8") as f:
            for term in data:
                f.write(json.dumps(term) + ",\n")

    def append_new_cleaned_data(clean_data,data):
        for term in clean_data:
            data.append(term)
        return data
