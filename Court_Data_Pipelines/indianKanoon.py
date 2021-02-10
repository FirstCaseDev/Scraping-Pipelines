from selenium import webdriver
import time
import datefinder
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
    judgement = driver.find_element_by_css_selector(".judgments")
    author = driver.find_element_by_css_selector(".doc_author").text
    bench = driver.find_element_by_css_selector(".doc_bench").text.split(':')[-1].split(',') # process
    title = driver.find_element_by_css_selector(".doc_title").text
    source = driver.find_element_by_css_selector(".docsource_main").text
    query_terms_elements = driver.find_elements_by_css_selector(".item_toselect") 
    p_tags = judgement.find_elements_by_tag_name("p")
    bq_tags = judgement.find_elements_by_tag_name("blockquote")
    paragraphs = p_tags + bq_tags
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
    case.judgement_text = judgement.text
    case.process_text()
    case.judgement_text_paragraphs = []
    for paragraph in paragraphs:
        case.judgement_text_paragraphs.append(paragraph.text)
    # case.print_case_attributes()
    driver.quit()
    return case

case = process_IndKanoon_url("https://indiankanoon.org/doc/145116477/")
case.print_case_attributes()
# store_case_document(case) #VERY DANGEROUS!!! DON'T UNCOMMENT UNLESS STORING TO DATABASE