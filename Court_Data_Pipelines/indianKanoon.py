from selenium import webdriver
import time
import datefinder
import re
import string
import pymongo
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.chrome.options import Options
from Common_Files.Case_handler import CaseDoc
from Common_Files.Case_storage import store_case_document
case = CaseDoc()

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
PATH = "C:\\Users\\punee\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(PATH,chrome_options=options) #Uncomment for Headless
# driver = webdriver.Chrome(PATH) #Uncomment for Windowed

def process_IndKanoon_url(url):
    case = CaseDoc()
    driver.get(url)
    judgement_div = driver.find_element_by_css_selector(".judgments")
    author = driver.find_element_by_css_selector(".doc_author").text.split(':')[-1].translate(str.maketrans('', '', string.punctuation)).strip()
    bench = driver.find_element_by_css_selector(".doc_bench").text.split(':')[-1].split(',|, |:|;|\\|')
    if '[' in bench[0]:
        bench = re.findall("\[(.*?)\]", bench[0])
    title = driver.find_element_by_css_selector(".doc_title").text
    source = driver.find_element_by_css_selector(".docsource_main").text
    query_terms_elements = driver.find_elements_by_css_selector(".item_toselect") 
    p_tags = judgement_div.find_elements_by_tag_name("p")
    pre_tags = judgement_div.find_elements_by_tag_name("pre")
    bq_tags = judgement_div.find_elements_by_tag_name("blockquote")
    pre_text = ""
    for pre_tag in pre_tags:
        pre_text = pre_text + "\n\n" + pre_tag.text
    pre_text_splitted = pre_text.replace('ACT:','>>>').replace('HEADNOTE:','>>>').replace('CITATION:','>>>').replace('JUDGEMENT:','>>>').split('>>>')
    paragraphs = p_tags[1:] + bq_tags
    for query_terms_element in query_terms_elements:
        case.query_terms.append(query_terms_element.text)  
    dates = datefinder.find_dates(title)
    for i in dates:
        date = i
    case.title = title
    case.petitioner = title.split(' vs ')[0].translate(str.maketrans('', '', string.punctuation)).strip()
    case.respondent = title.split(' vs ')[1].split(' on ')[0]
    case.date = date
    case.url = url
    case.doc_author = author
    case.bench = bench
    case.source = source
    case.judgement_text = judgement_div.text
    case.process_text() 
    case.judgement_text_paragraphs = []
    case.judgement_text_paragraphs.append(pre_text_splitted[0])
    for paragraph in paragraphs:
        case.judgement_text_paragraphs.append(paragraph.text)
    driver.quit()
    return case

case = process_IndKanoon_url("https://indiankanoon.org/doc/1386912/")
case.print_case_attributes()
# store_case_document(case) #VERY DANGEROUS!!! DON'T UNCOMMENT UNLESS STORING TO DATABASE