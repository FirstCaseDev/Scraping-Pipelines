from Common_Files.Case_handler import CaseDoc 
from elasticsearch import Elasticsearch
import pymongo
import json
#search singapore case from mongodb
#insert using elasticsearch index
from bson.objectid import ObjectId

case_object = CaseDoc()
class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        else:
            return obj

"""TODO: scroll all cases from mongodb, search cited case titles, experiment threshold, update documents: store in cases_referred"""

es = Elasticsearch(["https://search-firstcasecourtdata-fhx2m5ssjtso7lmalxrhhzrkmy.us-east-2.es.amazonaws.com"])
path = "mongodb://db_user:firstCaseDevTeam@107.20.44.181:27017,3.229.151.98:27017,54.175.129.116:27017/?authSource=admin&replicaSet=aName&readPreference=primaryPreferred&ssl=false"
client = pymongo.MongoClient(path)
db = client["indian_court_data"]
col = db["cases"]

cases_limit = 100
start_from = 0

while(1):
    print("page_number: " + str(start_from))
    cases_res = es.search(index="indian_court_data.cases", body={
                "_source": ["_id","title","cases_referred"],
                "from": start_from*cases_limit,
                "size": cases_limit,
                "query": {
                    "match": {
                    "source": "Delhi High Court"
                    }
                }
                }
                )
    for count,case_from_db in enumerate(cases_res["hits"]["hits"]):
        cited_cases_searched = 0
        cases_already_existed = 0
        cited_cases_found = 0
        cited_cases_not_found = 0
        case_object.cases_cited = case_from_db["_source"]["cases_referred"]
        case_object.title = case_from_db["_source"]["title"]
        case_object._id = case_from_db["_id"]
        for reffered_case_title in case_object.cases_cited:
            cited_cases_searched = cited_cases_searched + 1
            res = es.search(index="indian_court_data.cases", body={
                "_source": "title",
                "size": 5,
                "query": {
                    "match": {
                    "title": reffered_case_title
                    }
                }
                }
                )   
            if(res['hits']['hits'][0]['_score'] > 20):
                cited_cases_found = cited_cases_found + 1
                refferred_id = res['hits']['hits'][0]['_id']
                for refferred_case in col.find({"_id": ObjectId(refferred_id)}):
                    exists = 0
                    cases_citing = refferred_case['citing_cases']
                    for case_citing in cases_citing:
                        if (case_citing['_id']==str(case_object._id)):
                            exists = 1
                            cases_already_existed = cases_already_existed + 1
                            break
                    if(exists): 
                        break
                    cases_citing.append({"title":case_object.title, "_id":str(case_object._id)})
                    col.update_one({"_id":ObjectId(refferred_id)},{"$set":{"citing_cases":cases_citing}}, False, True)
                    break
            else:
                cited_cases_not_found = cited_cases_not_found + 1
        print("cases_processed in page: " + str(count+1))
        print("cited_cases_searched: " + str(cited_cases_searched))
        print("cited_cases_found: " + str(cited_cases_found))
        print("cases_cases_not_found: " + str(cited_cases_not_found))
        print("cases_already_existed: " + str(cases_already_existed))
        print("******************************************************")
    # break ##Comment for testing
    # if(start_from == 100):
    #     break
    start_from = start_from + 1



# for count,case_from_db in enumerate(col.find({"source":"Delhi High Court"})):
#     cited_cases_searched = 0
#     cases_already_existed = 0
#     cited_cases_found = 0
#     cited_cases_not_found = 0
#     case_object.cases_cited = case_from_db["cases_referred"]
#     case_object.title = case_from_db["title"]
#     case_object._id = case_from_db["_id"]
#     for reffered_case_title in case_object.cases_cited:
#         cited_cases_searched = cited_cases_searched + 1
#         res = es.search(index="indian_court_data.cases", body={
#             "_source": "title",
#             "size": 5,
#             "query": {
#                 "match": {
#                 "title": reffered_case_title
#                 }
#             }
#             }
#             )   
#         if(res['hits']['hits'][0]['_score'] > 20):
#             cited_cases_found = cited_cases_found + 1
#             refferred_id = res['hits']['hits'][0]['_id']
#             for refferred_case in col.find({"_id": ObjectId(refferred_id)}):
#                 exists = 0
#                 cases_citing = refferred_case['citing_cases']
#                 for case_citing in cases_citing:
#                     if (case_citing['_id']==str(case_object._id)):
#                         exists = 1
#                         cases_already_existed = cases_already_existed + 1
#                         break
#                 if(exists): 
#                     break
#                 cases_citing.append({"title":case_object.title, "_id":str(case_object._id)})
#                 print(col.update_one({"_id":ObjectId(refferred_id)},{"$set":{"citing_cases":cases_citing}}, False, True))
#                 break
#         else:
#             cited_cases_not_found = cited_cases_not_found + 1
#     print("cases_processed: " + str(count+1))
#     print("cited_cases_searched: " + str(cited_cases_searched))
#     print("cited_cases_found: " + str(cited_cases_found))
#     print("cases_cases_not_found: " + str(cited_cases_not_found))
#     print("cases_already_existed: " + str(cases_already_existed))
#     # break ##Comment for testing

