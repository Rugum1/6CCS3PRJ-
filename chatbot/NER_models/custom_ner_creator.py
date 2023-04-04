import spacy
import json
from spacy.lang.en import English
from spacy.pipeline import EntityRuler

#The code was taken from https://github.com/wjbmattingly/ner_youtube/blob/main/lessons/04_01_customizing_spacy.py, and adapted to the project. 
class NERCreator:

    file_dict = None
    ner_name = None

    def __init__(self,file_dict,ner_name):
        self.file_dict = file_dict
        self.ner_name = ner_name

    def load_data(self,file):
        with open(file , "r", encoding ="utf-8") as f:
            data = json.load(f)
        return(data)

    def create_pattern_data(self,file_dict):
        patterns = []
        for file in file_dict:
            type = file_dict[file]
            data = self.load_data(file)
            for cs_term in data:
                pattern = {
                            "label" : type,
                            "pattern" : cs_term
                          }
                patterns.append(pattern)
        return (patterns)

    def generate_rules(self,patterns,ner_name):
        nlp = English()
        ruler = nlp.add_pipe("entity_ruler")
        ruler.add_patterns(patterns)
        return nlp

    def save_ner(self,nlp,ner_name):
        nlp.to_disk(ner_name)

    def create_custom_NER_model(self):
        patterns = self.create_pattern_data(self.file_dict)
        nlp = self.generate_rules(patterns,self.ner_name)
        self.save_ner(nlp,self.ner_name)
        print("The NER model has been created succesfully")
