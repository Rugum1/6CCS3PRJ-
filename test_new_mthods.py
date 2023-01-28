import spacy 
from spacy.tokens import Doc

nlp = spacy.load("en_core_web_sm")
nlp.remove_pipe("ner")
nlp.add_pipe("entity_ruler", source=spacy.load("./NER_models/cs_ner_3"))
nlp.add_pipe('sentencizer')
doc = nlp("mutator method and overloading are two of the most significant ways that a method differs from a conventional procedure or function call. Overriding refers to a subclass redefining the implementation of a method of its superclass. For example, findArea may be a method defined on a shape class,[2] triangle, etc. would each define the appropriate formula to calculate their area. The idea is to look at objects as black boxes so that changes to the internals of the object can be made with minimal impact on the other objects that use it. This is known as encapsulation and is meant to make code easier to maintain and re-use. implicit type conversion") 
doc2 = nlp("mutator method")

# print(doc2.ents)
# for tok in doc: 
#     if tok.text not in list(doc2.ents): 
#         print(tok.text)

ents_list = list(doc.ents)
ents_list = [element.text for element in ents_list]

print(ents_list)


# for tok in doc: 
#     if tok.i < len(doc) - 1:
#         if (tok.text + " " + tok.nbor().text) in ents_list:
#              print(tok.text)
#         elif tok.text in ents_list:
#             print(tok.text)
    
   
# for tok in doc: 
#     j = 0
#     while 
#     print(tok.ent_iob_)

test_list = []


# for i in range(len(doc)): 



def pre_process(doc): 
    word_list = ""
    for tok in doc: 
        if not tok.is_punct:
            cleaned_word = "".join(c for c in tok.text if c.isalpha())
            # print(cleaned_word)
            word_list += " " + cleaned_word.lower().strip()
    
    return word_list.strip()




    


doc3 = nlp(pre_process(doc))
print(doc3)




for i in range(0,len(doc3)): 
    j = i
    if i < len(doc3):
        if doc3[j].ent_iob_ == "B":

            while j<len(doc3) and doc3[j].ent_iob_ != "O": 

                j+= 1 

            test_list.append(doc3[i:j].lemma_.strip())
            i = j 
        elif doc3[i].ent_iob_ != "I": 
             if not doc3[i].is_stop:
                 test_list.append(doc3[i].lemma_.strip())

# word =  " ".join(tok.lemma_ for tok in doc[0:3])
# print(word)

print(test_list)

    