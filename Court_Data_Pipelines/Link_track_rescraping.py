from selenium import webdriver
import datefinder
import re
import string
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from Common_Files.Case_handler import CaseDoc
from Common_Files.Case_storage import store_case_document
import datetime
case = CaseDoc()

missed_cases_count = 0
scraped_cases_count = 0
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
PATH = r"C:\\Program Files (x86)\\chromedriver.exe"
#PATH = "/root/chromedriver" ## only uncomment when on server
# driver = webdriver.Chrome(PATH,chrome_options=options) #Uncomment only this line for Headless
driver = webdriver.Chrome(PATH) #Uncomment only this line for Windowed
original_years_handle = ''
original_months_handle = ''
original_table_handle = ''
original_case_handle = ''
#TODO Only discard first pre tag
def process_IndKanoon_case_url(url):
    case = CaseDoc()
    script = "window.open('{0}', 'case_window')".format(url)
    driver.execute_script(script)
    original_case_handle = driver.window_handles[-2]
    driver.switch_to_window(driver.window_handles[-1])
    driver.set_page_load_timeout(60)
    try:
        try:
            source = driver.find_element_by_css_selector(".docsource_main").text
        except TimeoutException:
            print(url + " was partially loaded")
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
            if '[' in bench[0]:
                bench = re.findall("\[(.*?)\]", bench[0])
        except NoSuchElementException:
            print("no bench found")
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
            for query_terms_element in query_terms_elements:
                case.query_terms.append(query_terms_element.text)  
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
        dates = datefinder.find_dates(title)
        for i in dates:
            date = i
        try:
            case.title = title
            print(case.title)
        except:
            print("NO Title")
        try:
            case.petitioner = title.split(' vs ')[0].translate(str.maketrans('', '', string.punctuation)).strip()
        except:
            print("NO Petitioner")
        try:
            case.respondent = title.split(' vs ')[1].split(' on ')[0]
        except:
            print("NO respondent")
        try:
            case.date = date
            case.year = date.strftime("%Y")
            case.month = date.strftime("%B")
            case.day = date.strftime("%d")
        except:
            print("NO date")
        try:
            case.url = url
        except:
            print("NO URL")
        try:
            case.doc_author = author
        except:
            print("NO Author")
        try:
            case.bench = bench
        except:
            print("NO Bench")
        try:
            case.source = source
        except:
            print("NO Source")
        case.process_text() 
        store_case_document(case) #VERY DANGEROUS!!! DON'T UNCOMMENT UNLESS STORING TO DATABASE
        case.print_case_attributes()
    except Exception as inst:
        print(inst)
        open("indian_kanoon_missed_urls.txt", 'a+').write("%s\n" %(url) )
        print("Missed : %s\n" %(url) + (datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")) )
   
    driver.close()
    driver.switch_to_window(original_case_handle) 
    return case

def process_IndKanoon_paginated_table_url(url):
    # time.sleep(2)
    script = "window.open('{0}', 'table_window')".format(url)
    driver.execute_script(script)
    original_table_handle = driver.window_handles[-2]
    driver.switch_to_window(driver.window_handles[-1])
    try:
        total_case_mentioned = int(driver.find_element_by_css_selector("b:nth-child(1)").text.split('of')[-1])
        if total_case_mentioned > 400:
            current_url = driver.current_url
            print("Total Cases: " + str(total_case_mentioned) + " whose Url is : " + str(current_url))
            open("indian_kanoon_missed_400above_urls_patna.txt", 'a+').write("%s\n" %(current_url) )
    except:
        print("less than 400 or not having any case")
    
    driver.close()
    driver.switch_to_window(original_table_handle)

def process_IndKanoon_months_url(url):
    # time.sleep(2)
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
    # time.sleep(2)
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
url = "https://indiankanoon.org/browse/patna/"
process_IndKanoon_court_years_url(url)

# driver.get("https://www.google.com/") #any dummy url
# case = process_IndKanoon_case_url("https://indiankanoon.org/doc/105912122/")
# case.print_case_attributes()
# case = process_IndKanoon_case_url("https://indiankanoon.org/doc/871220/")
# case.print_case_attributes()
# case = process_IndKanoon_case_url("https://indiankanoon.org/doc/1902038/")
# case.print_case_attributes()

driver.quit()
print("Completed")
# store_case_document(case) #VERY DANGEROUS!!! DON'T UNCOMMENT UNLESS STORING TO DATABASE

# TODO: ADD TRY EXCEPT BLOCKS FOR TAGS EXTRACTION