import json, os, re, spacy

nlp = spacy.load("en_core_web_md")

file = open('last_request.json')
body = json.load(file)
# os.remove('./last_request.json')

queryText = body['queryResult']['queryText']
parameters = body['queryResult']['outputContexts'][0]['parameters']

input_array = queryText.split(" ")
for i in range(len(input_array)):
    input_array[i] = input_array[i].replace("?","").replace(",","")

relations = []; bench = []; petitioner = []; respondent = []; petitionerCounsel = []; respondentCounsel = []
spacy_entities = []; courts = []

def appendElem(array, elem):
    if not ((elem in bench) or (elem in petitioner) or (elem in respondent) or (elem in petitionerCounsel) or (elem in respondentCounsel) or (elem in courts) or (elem in countries)):
        array.append(elem)

def readAllEntities(doc):
    for entity in doc.ents:
        spacy_entities.append(entity.text)

def identifyCourts(spacy_entities):
    for elem in spacy_entities:
        for i in re.finditer('(((.*)(court))|((.*)(tribunal)(((\sfor(.*))?)))|((.*)(Commission))|((.*)(board)))', elem, re.IGNORECASE):
            courts.append(i.group())

def identifyParties(spacy_entities):
    for elem in spacy_entities:
        bench_score = 0; pet_score = 0; resp_score = 0; petCounsel_score = 0; respCounsel_score = 0
        pos = input_array.index(elem.split(" ")[0].strip())
        temp_string = ''
        temp_string = temp_string + input_array[pos-1] + ' '
        temp_string = temp_string + input_array[pos-3] + ' '

        # Benches
        for i in re.finditer('(justice)|(under)|(before)|(judge)', temp_string, re.IGNORECASE):
            # print("found " + i.group() + " bench for " + elem)
            bench_score = bench_score+2
            pet_score = pet_score-1 
            resp_score = resp_score-1
            petCounsel_score = petCounsel_score-1
            respCounsel_score = respCounsel_score-1

        # Petitioners
        for i in re.finditer('(by)|(filed)|(petitioner)', temp_string, re.IGNORECASE):
            # print("found " + i.group() + " petitioner for " + elem)
            bench_score = bench_score-1
            pet_score = pet_score+2
            resp_score = resp_score-1
            petCounsel_score = petCounsel_score-1
            respCounsel_score = respCounsel_score-1

        # Respondents
        for i in re.finditer('(against)|(filed)|(on)|(respondent)', temp_string, re.IGNORECASE):
            # print("found " + i.group() + " respondent for " + elem)
            bench_score = bench_score-1
            pet_score = pet_score-1 
            resp_score = resp_score+2
            petCounsel_score = petCounsel_score-1
            respCounsel_score = respCounsel_score-1

        # # Petitioners_Counsels
        # for i in re.finditer('(justice)|(under)|(before)|(judge)', temp_string, re.IGNORECASE):
        #     # print("found " + i.group() + " petitioner counsel for " + elem)
        #     bench_score = bench_score-1
        #     pet_score = pet_score-1 
        #     resp_score = resp_score-1
        #     petCounsel_score = petCounsel_score+2
        #     respCounsel_score = respCounsel_score-1

        # # Respondent_Counsels
        # for i in re.finditer('(justice)|(under)|(before)|(judge)', temp_string, re.IGNORECASE):
        #     # print("found " + i.group() + " respondent counsel for " + elem)
        #     bench_score = bench_score-1
        #     pet_score = pet_score-1 
        #     resp_score = resp_score-1
        #     petCounsel_score = petCounsel_score-1
        #     respCounsel_score = respCounsel_score+2  

        # print({
        #     'elem': elem,
        #     'pet_score': pet_score,
        #     'resp_score': resp_score,
        #     'bench_score': bench_score,
        #     'petCounsel_score': petCounsel_score,
        #     'respCounsel_score': respCounsel_score,
        # })   

        if bench_score > 1:
            appendElem(bench, elem)

        if (pet_score >= resp_score) and (pet_score > 0):
            appendElem(petitioner, elem)
            
        if (pet_score < resp_score) and (resp_score>0):
            appendElem(respondent, elem)

        if (petCounsel_score >= respCounsel_score) and (petCounsel_score >0):
            appendElem(petitionerCounsel, elem)

        if (petCounsel_score < respCounsel_score) and (respCounsel_score >0):
            appendElem(respondentCounsel, elem)


def getRelations(doc):
    for chunk in doc.noun_chunks:
        adj = []
        verb = []
        noun = ""
        for tok in chunk:
            if (tok.pos_ == "NOUN"):
                noun = tok.text
            if tok.pos_ == "ADJ":
                adj.append(tok.text)
            if tok.pos_ == "VERB":
                verb.append(tok.text)
        if noun:
            relations.append({'noun': noun, 'adj': adj, 'verb': verb})

doc = nlp(queryText)
getRelations(doc)
# print('\n\n')

countries = ['India']                                                      # India by default
if (parameters['geo-country'] != ""):
    countries = [elem for elem in parameters['geo-country']]

sortBy = 0                                                                 # 0: Most Recent (default), 1: Least Recent
if (parameters['CE-recency'] == "least recent"): sortBy = 1

legal_phrase = parameters['CE-legal-phrase']
persons = [person['name'] for person in parameters['person']]
readAllEntities(doc)
identifyCourts(spacy_entities)
identifyParties(spacy_entities)

# print("queryText:", queryText, '\n')
# print('countries:', countries, '\n')
# print('sortBy:', sortBy, '\n')
# print('legal_phrase:', legal_phrase, '\n')
# print('spacy_entities:', spacy_entities, '\n\n')
# print('bench:', bench, '\n')
# print('petitioner:', petitioner, '\n')
# print('respondent:', respondent, '\n')
# print('courts:', courts, '\n')

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

print(str(json.dumps(result)))


