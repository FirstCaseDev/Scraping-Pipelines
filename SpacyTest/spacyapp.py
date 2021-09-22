import flask
from flask import request
import json
import os
import re
import spacy
from elasticsearch import Elasticsearch

nlp = spacy.load("en_core_web_md")

app = flask.Flask(__name__)
app.config["DEBUG"] = True

es = Elasticsearch(
    ["https://search-firstcasecourtdata-fhx2m5ssjtso7lmalxrhhzrkmy.us-east-2.es.amazonaws.com/"])


def getCases(content):
    searchText = content['legal_phrase']
    courts = content['courts']
    # print(courts)
    judgements = content['judgements']
    sortBy = content['sortBy']
    countries = content['countries']
    judge = ''
    for elem in content['bench']:
        judge = judge + '(' + elem + ')' + '|'
    judge = judge[:-1]
    judge = '(' + judge + ')'
    # print(judge)

    ptnr = ''
    for elem in content['petitioner']:
        ptnr = ptnr + '(' + elem + ')' + '|'
    ptnr = ptnr[:-1]
    ptnr = '(' + ptnr + ')'
    # print(ptnr)

    resp = ''
    for elem in content['respondent']:
        resp = resp + '(' + elem + ')' + '|'
    resp = resp[:-1]
    resp = '(' + resp + ')'
    # print(resp)

    result = es.search(index="indian_court_data.cases",
                       body={
                           'track_scores': True,
                           'from': 0,
                           'size': 10,
                           '_source': [
                               "title",
                           ],
                           'query': {
                               'bool': {
                                   'must': [
                                       {
                                           'terms': {
                                               "source.keyword": ["Bombay High Court"],
                                           },
                                       },
                                       {
                                           'simple_query_string': {
                                               'query': searchText.strip(),
                                               'fields': [
                                                   "title^100",
                                                   "judgement_text",
                                                   "query_terms",
                                                   "citing_cases",
                                                   "cases_referred",
                                               ],
                                               'default_operator': "and",
                                           },
                                       },
                                   ],
                                   # Add Should
                                   # Add Filter
                               },
                           },
                           #    'script_fields': {
                           #        "_id ": {
                           #            'script': {
                           #                'lang': "painless",
                           #                'source': "doc['_id'].value",
                           #            },
                           #        },
                           #    },

                           #    'sort': [
                           #        {
                           #            '_script': {
                           #                'script': {
                           #                    'source':
                           #                    " double x = 7000*doc['citing_cases.title.keyword'].size() + 10*doc['cases_referred.keyword'].size(); int y = 0; if(doc['source.keyword'].value == 'Supreme Court of India') {y = 1000;} else if(doc['source.keyword'].value == 'Delhi High Court') { y =500;} else if(doc['source.keyword'].value == 'Bombay High Court') { y =500;} x+y+2*Float.parseFloat(doc['year.keyword'].value)+_score*100;",
                           #                    'lang': "painless",
                           #                },
                           #                'type': "number",
                           #                'order': "desc",
                           #            },
                           #        },
                           #    ],
                       })

    return {'response': result, 'content': content}


@app.route('/', methods=['GET'])
def home():
    return "hello"


@app.route('/', methods=['POST'])
def spacytest():
    # Define lists
    bench = []
    petitioner = []
    respondent = []
    petitionerCounsel = []
    respondentCounsel = []
    spacy_entities = []
    courts = []
    countries = []
    relations = []
    input_array = []

    body = request.json

    queryText = body['queryResult']['queryText']
    input_array = queryText.split(" ")
    for i in range(len(input_array)):
        input_array[i] = input_array[i].replace("?", "").replace(",", "")

    parameters = body['queryResult']['parameters']
    countries = ['India']           # India by default
    sortBy = 0                      # 0: Most Recent (default), 1: Least Recent

    doc = nlp(queryText)
    # getRelations(doc, relations)

    countries = [elem for elem in parameters['geo-country'] if (parameters['geo-country'] != "")] or ['India']
    sortBy = 1 if (parameters['CE-recency'] == "least recent") else 0
    legal_phrase = parameters['CE-legal-phrase']
    print(legal_phrase)

    # readAllEntities
    for entity in doc.ents:
        spacy_entities.append(entity.text)

    # identifyCourts
    for elem in spacy_entities:
        for i in re.finditer('(((.*)(court))|((.*)(tribunal)(((\sfor(.*))?)))|((.*)(Commission))|((.*)(board)))', elem, re.IGNORECASE):
            courts.append(i.group())
            spacy_entities.remove(elem)

    # identifyParties: re_strings order - 1) bench 2) petitioner 3) respondent 4) petitionerCounsel 5) respondentCounsel
    re_strings = ['(justice)|(under)|(before)|(judge)',
                  '(by)|(filed)|(petitioner)', '(against)|(filed)|(on)|(respondent)']
    for elem in spacy_entities:
        # bench_score = 0; pet_score = 0; resp_score = 0; petCounsel_score = 0; respCounsel_score = 0
        scores = [0, 0, 0, 0, 0]
        pos = input_array.index(elem.split(" ")[0].strip())
        temp_string = input_array[pos-1] + ' ' + input_array[pos-3]

        for i in range(len(re_strings)):
            for _ in re.finditer(re_strings[i], temp_string, re.IGNORECASE):
                scores = [n-1 for n in scores]
                scores[i] = scores[i] + 3

        if (scores[0] > 1) and ~(elem in bench):
            bench.append(elem)
            continue
        elif (scores[1] >= scores[2]) and (scores[1] > 0) and ~(elem in petitioner):
            petitioner.append(elem)
            continue
        elif (scores[1] < scores[2]) and (scores[2] > 0) and ~(elem in respondent):
            respondent.append(elem)
            continue

    judgements = parameters['CE-judgements']

    content = {
        "queryText": queryText,
        "countries": countries,
        "sortBy": sortBy,
        "legal_phrase": legal_phrase,
        "judgements": judgements,
        "spacy_entities": spacy_entities,
        "bench": bench,
        "petitioner": petitioner,
        "respondent": respondent,
        "courts": courts,
    }

    # print(content)

    abc = getCases(content)
    text = ''
    for elem in abc['response']['hits']['hits']:
        text = text + '\n\n' + elem['_source']['title']

    if text =='':
        text = "Sorry, but I didn't find anything related to this :("

    response = {
        "fulfillmentText": str(text),
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [str(text)],
                },
            },
        ],
        "abc": abc
    }

    return response


app.run()
