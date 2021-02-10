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
driver.get("https://indiankanoon.org/doc/137461156/")
case.judgement_text = driver.find_element_by_css_selector(".judgments").text
case.process_text()
print(len(case.judgement_text_paragraphs))
print(len(case.judgement_text))
print("cases cited : " + str(case.cases_cited))
print("provisions referred : " + str(case.provisions_referred))

