import string
import json
import re
import pymongo
client = pymongo.MongoClient("mongodb+srv://PuneetShrivas:admin@betatesting.nsnxl.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client["courtdata"]
col = db["cases"]

def compute_jaccard_sim(str_1, str_2):
    str_1_words = set(str_1.lower().strip().split())
    str_2_words = set(str_2.lower().strip().split())
    intersection = str_1_words & str_2_words
    union = str_1_words | str_2_words
    return len(intersection)/float(len(union))

count=0
titles_list = []
paragraphs_list = []
for count, doc in enumerate(col.find({"$text":{"$search":"Ambani"}})):
    judgement_text = doc['judgement_text']
    paragraphs = judgement_text.split('\n\n')
    print(judgement_text)
    title = doc['title']
    titles_list.append(title)
    print(count)

# similarites = []
# for title1 in titles_list:
#     for title2 in titles_list:
#         if(title1!=title2):
#             similarites.append({"title1":title1, "title2":title2, "similarity":compute_jaccard_sim(title1,title2)})

# similarites.sort(key=lambda json: json['similarity'], reverse=True)
# print(similarites)
# print(compute_jaccard_sim("My name isn't soumya", "My name is soumya"))
