from datetime import date,timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Common_Files.Case_pdf_handling import extract_txt
from Common_Files.Case_handler import CaseDoc
from Common_Files.Case_storage import store_case_document
from selenium.webdriver.chrome.options import Options
import datefinder
from selenium.common.exceptions import NoSuchElementException
import time


options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

PATH = "C:\Program Files (x86)\chromedriver.exe"

# driver = webdriver.Chrome(PATH,chrome_options=options) #Headless

driver = webdriver.Chrome(PATH)

def Singapore_Court():
    driver.get("https://www.singaporelawwatch.sg/Judgments")
    time.sleep(5)

def Court_of_appeal():
    body = driver.find_element_by_xpath('//*[@id="dnn_ctr449_ModuleContent"]/div')
Singapore_Court()
Court_of_appeal()    
