import flask
import json, os, re, spacy
nlp = spacy.load("en_core_web_md")

app = flask.Flask(__name__)
app.config["DEBUG"] = True
        
@app.route('/', methods=['GET'])
def home():
    return '''<h1>This is Home Page</h1>'''

@app.route('/', methods=['POST'])
def spacytest():
    # Define lists
    bench = []; petitioner = []; respondent = []; petitionerCounsel = []; respondentCounsel = []
    spacy_entities = []; courts = []; countries = []; relations = []; 
    input_array = []

    body = json.load(open('last_request.json'))

    queryText = body['queryResult']['queryText']
    input_array = queryText.split(" ")
    for i in range(len(input_array)):
        input_array[i] = input_array[i].replace("?","").replace(",","")

    parameters = body['queryResult']['outputContexts'][0]['parameters']
    countries = ['India']           # India by default
    sortBy = 0                      # 0: Most Recent (default), 1: Least Recent

    doc = nlp(queryText)
    # getRelations(doc, relations)

    countries = [elem for elem in parameters['geo-country'] if (parameters['geo-country'] != "")] or ['India']
    sortBy = 1 if (parameters['CE-recency'] == "least recent") else 0
    legal_phrase = parameters['CE-legal-phrase']

    # readAllEntities
    for entity in doc.ents:
        spacy_entities.append(entity.text)

    # identifyCourts
        for elem in spacy_entities:
            for i in re.finditer('(((.*)(court))|((.*)(tribunal)(((\sfor(.*))?)))|((.*)(Commission))|((.*)(board)))', elem, re.IGNORECASE):
                courts.append(i.group())

    # identifyParties
    re_strings = ['(justice)|(under)|(before)|(judge)','(by)|(filed)|(petitioner)','(against)|(filed)|(on)|(respondent)']   # order - 1) bench 2) petitioner 3) respondent 4) petitionerCounsel 5) respondentCounsel
    for elem in spacy_entities:
        scores = [0,0,0,0,0] # bench_score = 0; pet_score = 0; resp_score = 0; petCounsel_score = 0; respCounsel_score = 0
        pos = input_array.index(elem.split(" ")[0].strip())
        temp_string = input_array[pos-1] + ' '+ input_array[pos-3]

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
        elif (scores[1] < scores[2]) and (scores[2]>0) and ~(elem in respondent):
            respondent.append(elem)
            continue


    result = {
    "queryText": queryText,
    "countries": countries,
    "sortBy": sortBy,
    "legal_phrase": legal_phrase,
    "spacy_entities": spacy_entities,
    "bench": bench,
    "petitioner": petitioner,
    "respondent": respondent,
    "courts": courts,
    }

    print(result)
    response = {
          "fulfillmentText": "response generated",
          "fulfillmentMessages": [
            {
              "text": {
                "text": ["response generated"],
              },
            },
          ],
          "content": result,
        }

    return response


app.run()

