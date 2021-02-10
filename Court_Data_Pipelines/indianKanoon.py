from selenium import webdriver
import time
import pymongo
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.chrome.options import Options
from Common_Files.Case_handler import CaseDoc
case = CaseDoc()

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
PATH = "C:\\Users\\punee\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(PATH,chrome_options=options) #Headless
# driver = webdriver.Chrome(PATH) #Windowed
driver.get("https://indiankanoon.org/doc/1732220/")
judgement = driver.find_element_by_css_selector(".judgments")
case.judgement_text = judgement.text
case.process_text()
p_tags = judgement.find_elements_by_tag_name("p")
bq_tags = judgement.find_elements_by_tag_name("blockquote")
paragraphs = p_tags + bq_tags
case.judgement_text_paragraphs = []
for paragraph in paragraphs:
    case.judgement_text_paragraphs.append(paragraph.text)
print(len(case.judgement_text_paragraphs))
print("judgement : "  + str(case.judgement))
print("petitioner counsel : "  + str(case.petitioner_counsel))
print("respondent counsel : "  + str(case.respondent_counsel))
print("cases cited : " + str(case.cases_cited))
print("provisions referred : " + str(case.provisions_referred))

