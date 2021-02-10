import re
import regex
import spacy
import datetime
nlp = spacy.load('en_core_web_sm')
law_re_indicators = ['Act', 'Statute', 'Rules', 'Regulations', 'Reference', 'Constitution', 'Circular', 'Notice', 'Notification']
section_re_indicators = ['s\.', 'section', 'rule', 'article', 'chapter', 'clause', 'paragraph', 'explanation']
list_stop = ['of', 'for', 'the', 'and', 'under', '\.', ',', '\(', '\)', '\-']
list_stop_regex = '('+'|'.join(list_stop)+')'
first_cap_regex = '([A-Z]\S*\s*('+list_stop_regex+'*\s*'+'([A-Z]|\d)\S*\s*)+)'
law_regex_no_words = first_cap_regex+'(((,|of)\s+)?(\d)*\s*)*'
case_re_indicators = ['v', 'v\.', 'vs', 'vs\.', 'Vs', 'Vs\.', 'versus', 'Versus']

#****************************CASE CLASS DEFINITION****************************
class CaseDoc:
    def __init__(self):
        self.title = ""
        self.url = ""
        self.source = ""
        self.date = datetime.datetime.now()
        self.doc_author = "" 
        self.petitioner = ""
        self.respondent = ""
        self.bench = []
        self.petitioner_counsel = []
        self.respondent_counsel = []
        self.cases_cited = []
        self.cases_citing = []
        self.judgement = ""
        self.judgement_text = ""
        self.provisions_referred = []
    
    def process_text(self):
        print("*********processing text*********") 
        text = self.judgement_text.replace('\n', ' ').replace('\r','')
        self.cases_cited = case_get_cases_list(text)
        self.provisions_referred = case_get_acts_list(text)
        print("*********processed text*********") 



#****************************CASE SPECIFIC FUNCTIONS****************************
def case_get_acts_list(case_text):
    section_regexp = get_section_regexp(section_re_indicators)
    law_regexp = get_law_regexp(law_re_indicators)
    law_dict = {}
    try:
        doc_nlp = nlp(case_text)
        law_prev = ''
        for sent in doc_nlp.sents:
            txt_lower = sent.text.lower()
            sent_laws = find_laws(law_dict, sent.text, law_regexp)
            if re.search(section_regexp, sent.text, re.IGNORECASE):
                law_prev = find_section_and_law(law_dict, sent.text, section_regexp, law_regexp, law_prev, sent_laws)
            else:
                if len(sent_laws) > 0:
                    law_prev = sent_laws[-1][0]
    except: 
        print("oops parsing")
    combine_laws(law_dict)
    return repr_laws(law_dict)

def case_get_cases_list(case_text):
    case_regexp = get_case_regexp(case_re_indicators)
    case_list = []
    try:
        doc_nlp = nlp(case_text)
        for sent in doc_nlp.sents:
            txt_lower = sent.text.lower()
            if re.search(case_regexp, sent.text):
                case_list.extend(find_case(sent.text, case_regexp))
    except: 
        print("oops parsing")
    return case_list

def case_get_length(case_text):
    return(len(case_text)) 

#****************************HELPER FUNCTIONS****************************
def remove_stop(text):
    text = text.lower()
    text = re.sub(list_stop_regex, ' ', text)
    text = re.sub(' +', ' ', text)
    return text.strip()

def get_section_regexp(section_indicators):
    re_section_str = '('+'|'.join(section_indicators)+')'
    section_regexp = '(((\s|,|\.)+)'+re_section_str+'(\s+)(\S+)(\s?))((of|in)\s+(the\s+)?)?'
    # print (section_regexp)
    return section_regexp

def find_laws(law_dict, sent_text, law_regexp):
    sent_laws = []
    for m in re.finditer(law_regex_no_words, sent_text):
        law = m.group(0).strip()
        if re.search(law_regexp, law):
            if law not in law_dict:
                law_dict[law] = []
            sent_laws.append((law, m.start(), m.end()))
    return sent_laws

def get_law_regexp(law_re_indicators):
    return '('+'|'.join(law_re_indicators)+')'

def find_assoc_law(text):
    return re.match(law_regex_no_words, text)

def combine_laws(law_dict):
    init_keys = list(law_dict.keys())
    mapping = {}
    for law in init_keys:
        law_norm = remove_stop(law)
        if law_norm in law_dict:
            if mapping[law_norm][1] < len(law_dict[law]):
                mapping[law_norm] = (law, len(law_dict[law]))
            law_dict[law_norm].extend(law_dict[law])
        else:
            mapping[law_norm] = (law, len(law_dict[law]))
            law_dict[law_norm] = law_dict[law][:]
        del law_dict[law]
    new_keys = list(law_dict.keys())
    for law in new_keys:
        law_dict[mapping[law][0]] = law_dict.pop(law)

def find_section_and_law(law_dict, sent_text, section_regexp, law_regexp, law_prev, sent_laws):
    curr_idx = -1
    if len(sent_laws) > 0:
        curr_idx = 0
    for m in re.finditer(section_regexp, sent_text, re.IGNORECASE):
        if curr_idx >= 0:
            while curr_idx < len(sent_laws) and m.start() > sent_laws[curr_idx][2]:
                law_prev = sent_laws[curr_idx][0]
                curr_idx += 1
        section_str = m.group(1).strip()
        if m.group(6):
            assoc_law = find_assoc_law(sent_text[m.end():])
            if assoc_law: 
                curr_law = assoc_law.group(0).strip()
                if re.search(law_regexp, curr_law):
                    law_prev = curr_law
                else:
                    section_str += ', '+curr_law
        if len(law_prev) > 0 and law_prev not in law_dict:
            law_dict[law_prev] = []
        if len(law_prev) > 0:
            law_dict[law_prev].append(section_str)
    if len(sent_laws) > 0:
        law_prev = sent_laws[-1][0]
    return law_prev    

def repr_laws(law_dict):
    str_laws_with_sections = ""
    for law in law_dict:
        str_laws_with_sections += law+':'
        str_laws_with_sections += '|'.join(law_dict[law]) + ';'
    return str_laws_with_sections[:-1]

def get_case_regexp(case_indicators):
    re_case_str = '('+'|'.join(case_indicators)+')'
    case_regexp = '(\s+)'+re_case_str+'(\s+)'
    # print (case_regexp)
    return case_regexp

def find_case(sent_text, case_regexp):
    list_cases = []
    last_case = ''
    for m in re.finditer(case_regexp, sent_text):
        first_case = find_last_set_cap_words(sent_text[:m.start()])
        if first_case and ' and ' in first_case and first_case.strip() == last_case.strip():
            curr = first_case.split(' and ')
            try:
                past_case_split = list_cases[-1].split(mid)
                list_cases[-1] = past_case_split[0]+mid+curr[0]
            except:
                #print "oops case"
                pass
            first_case = curr[1]
        mid = m.group(0)
        last_case = find_first_set_cap_words(sent_text[m.end():])
        if first_case and mid and last_case:
            list_cases.append(first_case.strip()+mid+last_case.strip())
        else:
            print (first_case, mid, last_case)
    return list_cases

def find_last_set_cap_words(str_in):
    m = re.findall(first_cap_regex, str_in)
    if m:
        if len(m) > 0:
            return m[-1][0]
    return None

def find_first_set_cap_words(str_in):
    m = re.findall(first_cap_regex, str_in)
    if m:
        if len(m) > 0:
            return m[0][0]
    return None