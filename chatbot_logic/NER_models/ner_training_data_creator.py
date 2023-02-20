import json
from spacy.matcher import PhraseMatcher
import spacy
from spacy.matcher import Matcher

# class NERTrainingDataCreator:
#
#     def load_data(self,file):
#         with open(file , "r", encoding ="utf-8") as f:
#             data = json.load(f)
#         return(data)
#
#     def save_data(self,file,data):
#         with opent(file, "w", encoding = "utf-8") as f:
#             json.dump(data,f,indent = 4)
#
#     def test_model(model,text):
#         doc = nlp(text)
#         results = []
#         for ent in doc.ents:


def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return (data)

def save_data(file, data):
    with open (file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def test_model(model, text):
    doc = nlp(text)
    results = []
    entities = []

    for ent in doc.ents:
        entities.append((ent.start_char, ent.end_char, ent.label_))
        print((ent.text,ent.start_char, ent.end_char, ent.label_,))
    if len(entities) > 0:
        results = [text, {"entities": entities}]

        return (results)

#TRAIN_DATA = [(text, {"entities": [(start, end, label)]})]

nlp = spacy.load("NER_models/java_ner")
TRAIN_DATA = []
with open ("./data/object_first.txt", "r")as f:
    text = f.read()

    chapters = text.split("CHAPTER")
    for chapter in chapters:
        chapter_num, chapter_title = chapter.split("\n\n")[0:2]
        chapter_num = chapter_num.strip()
        segments = chapter.split("\n\n")[2:]
        hits = []
        for segment in segments:
            segment = segment.strip()
            segment = segment.replace("\n", " ")
            results = test_model(nlp, segment)

            if results != None:
                TRAIN_DATA.append(results)
#
print (len(TRAIN_DATA))


# text = "abstract methods have no implementation. The sky is blue"
#
# nlp = spacy.load("NER_models/cs_ner_2")
#
# phrase_matcher = PhraseMatcher(nlp.vocab)
# phrases = ['']
# patterns = [nlp(text) for text in phrases]
# phrase_matcher.add('AI', None, *patterns)
#
# with open ("./data/object_first.txt", "r")as f:
#     text = f.read()
#     chapters = text.split("CHAPTER")
#     for chapter in chapters:
#         segments = chapter.split("\n\n")[2:]
#         for segment in segments:
#             doc = nlp(segment)
#         for ent in doc.ents:
#             if ent.text == 'private':
#                 for sent in doc.sents:
#                     for match_id, start, end in phrase_matcher(nlp(sent.text)):
#                         if nlp.vocab.strings[match_id] in ["AI"]:
#                           print(sent.text)
