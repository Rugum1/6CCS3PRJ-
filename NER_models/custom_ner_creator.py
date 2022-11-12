import spacy
import json
from spacy.lang.en import English
from spacy.pipeline import EntityRuler


class NERCreator:

    type = None
    file = None
    ner_name = None

    def __init__(self,type,file,ner_name):
        self.type = type
        self.file = file
        self.ner_name = ner_name

    def create_custom_NER_model(self):
        patterns = create_training_data(self.file, self.type)
        generate_rules(patterns,self.ner_name)
        print("The NER model has been created succesfully")

    def load_data(self,file):
        with open(file , "r", encoding ="utf-8") as f:
            data = json.load(f)
        return(data)


    #This method was taken from Python tutorials for digital humanities
    def create_training_data(self,file,type):
        data = load_data(file)
        patterns = []
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
        nlp.to_disk(ner_name)
