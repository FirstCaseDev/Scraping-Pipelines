from elasticsearch import Elasticsearch
import pymongo
import json
#search singapore case from mongodb
#insert using elasticsearch index
from bson.objectid import ObjectId

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
print("Searching")
case = json.loads(json.dumps(col.find_one({"source":"Supreme Court Singapore"}), cls=Encoder))
res = es.index(index="indian_court_data.cases", doc_type="Any",body=case)
print(res)


