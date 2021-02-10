import pymongo


def store_case_document(case):
    client = pymongo.MongoClient("mongodb+srv://PuneetShrivas:admin@betatesting.nsnxl.mongodb.net/<dbname>?retryWrites=true&w=majority")
    db = client["indian_court_data"]
    col = db["cases"]
    print(str(col.insert_one(case)))

def case_exists_by_url(url):
    client = pymongo.MongoClient("mongodb+srv://PuneetShrivas:admin@betatesting.nsnxl.mongodb.net/<dbname>?retryWrites=true&w=majority")
    db = client["indian_court_data"]
    col = db["cases"]
    if(col.find({"url": url}).count()>0):
        return 1
    else:
        return 0

def case_exists_by_title(title):
    client = pymongo.MongoClient("mongodb+srv://PuneetShrivas:admin@betatesting.nsnxl.mongodb.net/<dbname>?retryWrites=true&w=majority")
    db = client["indian_court_data"]
    col = db["cases"]
    if(col.find({"title": title}).count()>0):
        return 1
    else:
        return 0