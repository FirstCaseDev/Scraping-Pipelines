from selenium import webdriver
import time
import datetime
import datefinder
import pymongo
from Common_Files.Case_pdf_handling import extract_txt
from Common_Files.Case_storage import store_case_document, case_exists_by_case_id
from Common_Files.Case_handler import CaseDoc 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located


#accessing Case_storage database
client = pymongo.MongoClient('mongodb://db_user:firstCaseDevTeam@107.20.44.181:27017,3.229.151.98:27017,54.175.129.116:27017/?authSource=admin&replicaSet=aName&readPreference=primaryPreferred&ssl=false')
db = client["indian_court_data"]
col = db["cases"]


#for headless
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

#setting up the driver
PATH='C://Program Files (x86)//chromedriver.exe'
driver= webdriver.Chrome(PATH)

#Headless
#driver = webdriver.Chrome(PATH,chrome_options=options) 

#opening an instance @ncalt.nic.in --> Judgements
driver.get('https://www.aptel.gov.in/old-judgement-data')
time.sleep(1)

'''
#year selection 2010(option[2])--2031(option[23])
driver.find_element_by_xpath('//*[@id="edit-field-judge-yeras-value-value-year"]').click()
year = driver.find_element_by_xpath('//*[@id="edit-field-judge-yeras-value-value-year"]/option[13]')
year.click()
time.sleep(1)
'''

#apply button
driver.find_element_by_xpath('//*[@id="edit-submit-judgements-orders"]').click()

#scrapping page's data
case=CaseDoc()

#loacting target table for scrapping
table=driver.find_element_by_xpath('//*[@id="block-system-main"]/div/div/div[2]/table')
t_body=table.find_element_by_tag_name('tbody')

rows=t_body.find_elements(By.TAG_NAME,'tr')

#counter for table's rows
tr_counter=0

for row in rows:
    tr_counter+=1
    #print(tr_counter)

    #(ambiguous condition---> however, it works!)
    if tr_counter>=3:
        #accessing td tags for each row
        tds=row.find_elements(By.TAG_NAME, 'td')
        td_counter=0

        for td in tds:
            
            td_counter+=1

            #case number and pdf link
            if td_counter==2:
                #caes no.
                temp=[]
                temp.append(td.text)
                print('Case id                  :', temp[0])
                #case.case_id=temp[0]

                #pdf_link
                a_tags=td.find_elements(By.TAG_NAME,'a')

                for a_tag in a_tags:
                    pdf_link=a_tag.get_attribute('href')
                    print('Pdf link                 :', pdf_link)
                    #case.url=pdf_link
                    #judgement_txt=extract_txt(pdf_link, 'Court_Extract.pdf')
                    #case.judgement_text=judgement_txt


            #petitioner & respondent
            if td_counter==3:
                temp=[]
                temp.append(td.text)
                temp_str=temp[0]
                #print(temp_str)
                slice_1=temp_str.find('Versus')
               
                print('Petitioner               :', temp_str[0:slice_1-2])
                print('Respondent               :', temp_str[slice_1+7:])
                #case.petitioner = temp_str[0:slice_1-2]
                #case.respondent = temp_str[slice_1+7:]


            #date of judgement
            if td_counter==5:
                temp=[]
                temp.append(td.text)
                k= temp[0]
                slice_1 = k.find('-----------------')
                jud_date=k[0:slice_1]
                print('Date                     :', jud_date)

                date=datefinder.find_dates(jud_date)
                for i in date:
                    date=i 
                #case.date=date
                #case.year = date.strftime("%Y")

        #spacing b/w cases
        print()

        #processing all the extracted data
        #case.process_text()
        #case.print_case_attributes()
        #store_case_document(case)

#closing chrome istance/window
driver.quit()

        














