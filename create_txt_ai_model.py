from txtai.embeddings import Embeddings
from txtai.pipeline import Extractor
import csv



embeddings =Embeddings({

    "path" : "sentence-transformers/all-MiniLM-L6-v2"

})
embeddings.load("index_cs_data")
extractor = Extractor(embeddings, "distilbert-base-cased-distilled-squad")

f1= "./data/computer_science_dataset.csv"
txt_data = []
j = 0
with open(f1,'r') as file_obj:

    # Create reader object by passing the file
    # object to DictReader method
    reader_obj = csv.DictReader(file_obj)


    for row in reader_obj:
        txt_data.append(row["paragraph"])
        j+=1

# embeddings.index(txt_data)
# embeddings.save("index_cs_data")

question = "What is object oriented programming?"

# execute = lambda query: extractor([(question, query, question, False) for question in questions],txt_data)

embeddings.load("index_cs_data")

print(extractor([(question, question, question, False)], txt_data))
# #
# res = embeddings.search("",10)
# # print(res)
# #
# for item in res:
#     print(txt_data[item[0]],"<->", item[1])
#     print()
