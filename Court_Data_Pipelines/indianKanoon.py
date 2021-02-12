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
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from Common_Files.Case_handler import CaseDoc
from Common_Files.Case_storage import store_case_document
case = CaseDoc()

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
PATH = "C:\\Users\\punee\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(PATH,chrome_options=options) #Uncomment only this line for Headless
# driver = webdriver.Chrome(PATH) #Uncomment only this line for Windowed
original_years_handle = ''
original_months_handle = ''
original_table_handle = ''
original_case_handle = ''

def process_IndKanoon_case_url(url):
    case = CaseDoc()
    script = "window.open('{0}', 'case_window')".format(url)
    driver.execute_script(script)
    original_case_handle = driver.window_handles[-2]
    driver.switch_to_window(driver.window_handles[-1])
    driver.set_page_load_timeout(10)
    try:
        source = driver.find_element_by_css_selector(".docsource_main").text
    except TimeoutException:
        print(url + " was partially loaded")
        # driver.execute_script("return window.stop")
    try:
        judgement_div = driver.find_element_by_css_selector(".judgments")
    except NoSuchElementException: 
        print("no judgement")
    try:
        author = driver.find_element_by_css_selector(".doc_author").text.split(':')[-1].translate(str.maketrans('', '', string.punctuation)).strip()
    except NoSuchElementException:
        print("no author found")
    try:
        bench = driver.find_element_by_css_selector(".doc_bench").text.split(':')[-1].split(',')
    except NoSuchElementException:
        print("no bench found")
    if '[' in bench[0]:
        bench = re.findall("\[(.*?)\]", bench[0])
    try:
        title = driver.find_element_by_css_selector(".doc_title").text
    except NoSuchElementException:
        print("no title found")
    try:
        source = driver.find_element_by_css_selector(".docsource_main").text
    except NoSuchElementException:
        print("no source found")
    try:
        query_terms_elements = driver.find_elements_by_css_selector(".item_toselect") 
    except NoSuchElementException:
        print("no query terms found")
    try:
        p_tags = judgement_div.find_elements_by_css_selector("blockquote, p")
        pre_tags = judgement_div.find_elements_by_tag_name("pre")
    except NoSuchElementException:
        pass
    pre_text = ""
    for pre_tag in pre_tags:
        pre_text = pre_text + "\n\n" + pre_tag.text
    pre_text_splitted = pre_text.replace('ACT:','>>>').replace('HEADNOTE:','>>>').replace('CITATION:','>>>').replace('JUDGEMENT:','>>>').split('>>>')
    paragraphs = p_tags[1:]
    judgement_text_paragraphs = []
    judgement_text_paragraphs.append(pre_text_splitted[0])
    for paragraph in paragraphs:
        judgement_text_paragraphs.append(paragraph.text.replace('\n','').replace('\r','').replace('',''))
    case.judgement_text = ' >>>> '.join(judgement_text_paragraphs)
    for query_terms_element in query_terms_elements:
        case.query_terms.append(query_terms_element.text)  
    dates = datefinder.find_dates(title)
    for i in dates:
        date = i
    case.title = title
    print(case.title)
    case.petitioner = title.split(' vs ')[0].translate(str.maketrans('', '', string.punctuation)).strip()
    case.respondent = title.split(' vs ')[1].split(' on ')[0]
    case.date = date
    case.url = url
    case.doc_author = author
    case.bench = bench
    case.source = source
    case.process_text() 
    case.print_case_attributes()
    
    driver.close()
    driver.switch_to_window(original_case_handle)
    return case

def process_IndKanoon_paginated_table_url(url):
    time.sleep(2)
    script = "window.open('{0}', 'table_window')".format(url)
    driver.execute_script(script)
    original_table_handle = driver.window_handles[-2]
    driver.switch_to_window(driver.window_handles[-1])
    total_case_mentioned = int(driver.find_element_by_css_selector("b:nth-child(1)").text.split('of')[-1])
    # print("Total Cases: " + str(total_case_mentioned))
    case_count_in_table = 0
    found_next_page = True
    while(found_next_page):
        case_tags = driver.find_elements_by_css_selector(".result_title a")
        case_count_in_table = case_count_in_table + len(case_tags)
        current_count = 1
        for case_tag in case_tags:
            case_url = case_tag.get_attribute("href")
            # print("...#" + str(current_count) + " of total " + str(total_case_mentioned) + "cases...")
            case = process_IndKanoon_case_url(case_url)
            # store_case_document(case) #VERY DANGEROUS!!! DON'T UNCOMMENT UNLESS STORING TO DATABASE
            current_count = current_count + 1
        try:
            next_page_tag_url = driver.find_element_by_css_selector(".pagenum+ a").get_attribute("href")
            driver.get(next_page_tag_url)
        except NoSuchElementException:
            print("...cases missed in scraping :" + str(total_case_mentioned - case_count_in_table))
            found_next_page = False
    driver.close()
    driver.switch_to_window(original_table_handle)

def process_IndKanoon_months_url(url):
    time.sleep(2)
    script = "window.open('{0}', 'month_window')".format(url)
    driver.execute_script(script)
    original_months_handle = driver.window_handles[-2]
    driver.switch_to_window(driver.window_handles[-1])
    month_tags = driver.find_elements_by_css_selector(".browselist a")
    for month_tag in month_tags:
        print(month_tag.text)
        paginated_table_url = month_tag.get_attribute("href")
        process_IndKanoon_paginated_table_url(paginated_table_url)
    driver.close()
    driver.switch_to_window(original_months_handle)

def process_IndKanoon_court_years_url(url):
    time.sleep(2)
    script = "window.open('{0}', 'year_window')".format(url)
    driver.execute_script(script)
    original_years_handle = driver.window_handles[-2]
    driver.switch_to_window(driver.window_handles[-1])
    year_tags = driver.find_elements_by_css_selector(".browselist a")
    for year_tag in year_tags:
        print(year_tag.text)
        month_url = year_tag.get_attribute("href")
        process_IndKanoon_months_url(month_url)
    driver.close()
    driver.switch_to_window(original_years_handle)

# driver.get("https://indiankanoon.org/browse/")
# court_tags = driver.find_elements_by_css_selector(".browselist") 
# for court_tag in court_tags:
#     print(court_tag.text)
#     court_url = court_tag.find_element_by_tag_name("a").get_attribute("href")
#     process_IndKanoon_court_years_url(court_url)

driver.get("https://www.google.com/") #any dummy url
case = process_IndKanoon_case_url("https://indiankanoon.org/doc/126137620/")
# case.print_case_attributes()
case = process_IndKanoon_case_url("https://indiankanoon.org/doc/871220/")
# case.print_case_attributes()
# case = process_IndKanoon_case_url("https://indiankanoon.org/doc/1902038/")
# case.print_case_attributes()

driver.quit()
# store_case_document(case) #VERY DANGEROUS!!! DON'T UNCOMMENT UNLESS STORING TO DATABASE

# TODO: ADD TRY EXCEPT BLOCKS FOR TAGS EXTRACTION