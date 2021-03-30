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

PATH = r"C:\\Program Files (x86)\\chromedriver.exe"

# driver = webdriver.Chrome(PATH,chrome_options=options) #Headless

driver = webdriver.Chrome(PATH)

def Singapore_Court():
    driver.get("https://www.singaporelawwatch.sg/Judgments")
    time.sleep(5)

def Court_of_appeal():
    body = driver.find_element_by_xpath('//*[@id="dnn_ctr449_ModuleContent"]/div/div[1]')
    articles = body.find_elements_by_tag_name("article")
    for article in articles:
        print("Doneeee")
        print(article.text)
        print("DOne2")
        a_tags = article.find_elements_by_tag_name("a")
        print("suivhbie")
        for a_tag in a_tags:
            count = count + 1
            
            
            link = a_tag.get_attribute("href")
            print("Doneeeeeeee")
            print("Doneeeeeeee")
            print(a_tags.text)
            print("Doneeeeeeee")
            print("Doneeeeeeee")
            print(link)
            
            print(count)
            

def High_Court():
    body = driver.find_element_by_xpath('//*[@id="dnn_ctr450_ModuleContent"]/div/div[1]')
    articles = body.find_elements_by_tag_name('article')
    print("done123134123")
    for article in articles:
        a_tag = article.find_elements_by_xpath('//*[@id="dnn_ctr450_ModuleContent"]/div/div[1]/article[1]/h4/a')
        link = a_tag.get_attribute("href")
        print(link)
        print(a_tag.text)



Singapore_Court()

# for i in range(2):  ## 280 because total pages are 281 and have to click next 280 times
#     try:
#         Court_of_appeal()
#         print('try1') 
#         try:
#             print("try2") 
#             body = driver.find_element_by_xpath('/html/body/form/div[5]/div[10]/div/div[1]/div/div/div[3]/div/div[1]/div/div')
#             while (body.find_element_by_link_text("Next").click() == None):
#                 body.find_element_by_link_text("Next")
#                 print("while1")
#                 Court_of_appeal() 
#                 print("While2")
        
#         except:
#             print("except!")
#             time.sleep(20)
#             continue
#     except:
#         print("except2")
#         continue    



Singapore_Court()
for i in range(1275):  ## 280 because total pages are 281 and have to click next 280 times
    try:
        High_Court() 
        try: 
            body = driver.find_element_by_xpath('/html/body/form/div[5]/div[10]/div/div[1]/div/div/div[4]/div/div[1]/div/div/div[2]')
            while (body.find_element_by_link_text("Next").is_displayed() == True):
                body.find_element_by_link_text("Next").click()
                High_Court()
        except:
            continue
    except:
        continue    