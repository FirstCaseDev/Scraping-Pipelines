import string
import json
import re
import pymongo
client = pymongo.MongoClient("mongodb+srv://PuneetShrivas:admin@betatesting.nsnxl.mongodb.net/<dbname>?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb://{username}:{password}@3.136.112.164/indian_court_data")
db = client["indian_court_data"]
col = db["cases"]



# def compute_jaccard_sim(str_1, str_2):
#     str_1_words = set(str_1.lower().strip().split())
#     str_2_words = set(str_2.lower().strip().split())
#     intersection = str_1_words & str_2_words
#     union = str_1_words | str_2_words
#     return len(intersection)/float(len(union))

# count=0
# titles_list = []
# paragraphs_list = []
# for count, doc in enumerate(col.find()):#{"$text":{"$search":"Ambani"}}
#     judgement_text = doc['judgement_text']
#     paragraphs = judgement_text.split('>>>>')#\n\n
#     # print(len(paragraphs))
#     # title = doc['title']
#     for paragraph in paragraphs:
#         paragraphs_list.append(paragraph)
#     # print(count)

# similarites = []
# for paragraph1 in paragraphs_list:
#     for paragraph2 in paragraphs_list:
#         if(paragraph1!=paragraph2):
#             similarites.append({"paragraph1":paragraph1, "paragraph2":paragraph2, "similarity":compute_jaccard_sim(paragraph1,paragraph2)})


# similarites.sort(key=lambda json: json['similarity'], reverse=True)
# print(similarites[:30])
# #TODO compute sum of similarities and then sort for each paragraph
