import sys
import spacy
import json
import re

# Functions
def getCourtsPhrases(total_text):
    for elem in total_text:
        for i in re.finditer('(((.*)(court))|((.*)(tribunal)(((\sfor(.*))?)))|((.*)(Commission))|((.*)(board)))', elem, re.IGNORECASE):
            courts.append(i.group())

def getPersons(entities):
    for elem in entities:
        bench_score = 0; pet_score = 0; resp_score = 0; petCounsel_score = 0; respCounsel_score = 0
        # print(input_array)
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
        for i in re.finditer('(by)|(filed)|(petitioner)', elem, re.IGNORECASE):
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

        # Petitioners_Counsels
        for i in re.finditer('(justice)|(under)|(before)|(judge)', elem, re.IGNORECASE):
            # print("found " + i.group() + " petitioner counsel for " + elem)
            bench_score = bench_score-1
            pet_score = pet_score-1 
            resp_score = resp_score-1
            petCounsel_score = petCounsel_score+2
            respCounsel_score = respCounsel_score-1

        # Respondent_Counsels
        for i in re.finditer('(justice)|(under)|(before)|(judge)', elem, re.IGNORECASE):
            # print("found " + i.group() + " respondent counsel for " + elem)
            bench_score = bench_score-1
            pet_score = pet_score-1 
            resp_score = resp_score-1
            petCounsel_score = petCounsel_score-1
            respCounsel_score = respCounsel_score+2     

        if bench_score > 1:
            bench.append(elem)

        if pet_score >= resp_score:
            petitioner.append(elem)
            
        if pet_score < resp_score:
            respondent.append(elem)

        if petCounsel_score >= respCounsel_score:
            petitioner_counsel.append(elem)

        if petCounsel_score < respCounsel_score:
            respondent_counsel.append(elem)

def getCountry(entities):
    for elem in entities:
        if (elem['label'] == "GPE"):
            country.append(elem['name'])

nouns = []; verbs = []; persons = []; entities = []
total_text = []
courts = []
bench = []
judgments = []
country = []
states = []
petitioner_counsel = []
respondent_counsel = []
petitioner = []
respondent = []
dates = []
text_to_process = []

entities_text = []

nlp = spacy.load("en_core_web_sm")
input_array = sys.argv
input_array.pop(0)

# Complete Text
# What is the law on divorce cases in India since 2018 under supreme court?
text = ''
for elem in input_array:
    text = text + " " + elem.replace("?","")

input_array = text.split(" ")

# input_array contains all the words sequentially
# check on each word if its noun, verb, or entity

doc = nlp(text)
for chunk in doc.noun_chunks:
    nouns.append(chunk.text)
    total_text.append(chunk.text)

for token in doc:
    if token.pos_ == "VERB":
        verbs.append(token.lemma_)
        total_text.append(token.lemma_)

for entity in doc.ents:
    entities.append({'name': entity.text, 'label': entity.label_, 'description': spacy.explain(entity.label_)})
    entities_text.append(entity.text)
    total_text.append(entity.text)

total_text = list(set(total_text))
getCourtsPhrases(total_text)
getPersons(entities_text)
getCountry(entities)

result = {
    'nouns': nouns,
    # 'verbs': verbs,
    # 'persons': persons,
    'text': total_text,
    'entities': entities,
    'courts': courts,
    'bench': bench,
    'respondent': respondent,
    'country': country,
}

spacy.displacy.serve(doc, style="ent")
