import pymongo


def store_case_document(case):
    client = pymongo.MongoClient("mongodb+srv://PuneetShrivas:admin@betatesting.nsnxl.mongodb.net/<dbname>?retryWrites=true&w=majority")
    db = client["indian_court_data"]
    col = db["cases"]
    data_object = {
        "title": case.title,
        "case_id": case.case_id,
        "url": case.url,
        "source": case.source,
        "date": case.date,
        "doc_author": case.doc_author,
        "petitioner": case.petitioner,
        "respondent": case.respondent,
        "bench": case.bench,
        "petitioner_counsel": case.petitioner_counsel,
        "respondent_counsel": case.respondent_counsel,
        "cases_referred": case.cases_cited,
        "citing_cases": case.cases_citing,
        "judgement": case.judgement,
        "judgement_text": case.judgement_text,
        # "judgement_text_paragraphs": case.judgement_text_paragraphs,
        "provisions_referred": case.provisions_referred,
        "query_terms": case.query_terms
    }
    print(str(col.insert_one(data_object)))

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

def case_exists_by_case_id(case_id):
    client = pymongo.MongoClient("mongodb+srv://PuneetShrivas:admin@betatesting.nsnxl.mongodb.net/<dbname>?retryWrites=true&w=majority")
    db = client["indian_court_data"]
    col = db["cases"]
    if(col.find({"case_id": case_id}).count()>0):
        return 1
    else:
        return 0