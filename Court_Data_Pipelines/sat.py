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


#opening an instance @http://sat.gov.in/
driver.get('http://sat.gov.in/')
time.sleep(1)


#calculating current month
current_day = datetime.date.today()
current_month_index = int(current_day.strftime('%m'))
#print(current_day)


#souces/departments present on the site
sources = ['SEBI', 'IRDAI', 'PFRDA']


#scrapping page's data
case=CaseDoc()

#for accessing different departments (SEBI, IRDAI, PFRDA)
for dep in range(1,4):

    #accessing dep one by one
    driver.find_element_by_xpath('/html/body/table[4]/tbody/tr/td[3]/div[2]/a[{DEP_INDEX}]'.format(DEP_INDEX = dep)).click()
    time.sleep(1)

    #selecting month
    driver.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[2]/td/p/font/select[2]').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[2]/td/p/font/select[2]/option[{month_index}]'.format(month_index = current_month_index)).click()
    
    #go buttton
    driver.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[2]/td/p/font/input').click()
    time.sleep(1)

    #loacting target table for scrapping
    table=driver.find_element_by_xpath('//*[@id="form1"]/table')
    t_body=table.find_element_by_tag_name('tbody')
    rows=t_body.find_elements(By.TAG_NAME,'tr')

    
    '''
    #coumting total no. of rows
    total_rows=0
    for x in rows:
        total_rows+=1
    '''
    
    row_counter=0

    for row in rows:

        row_counter+=1
        row_text= row.text
        
        if (row_counter>=4) and (row_counter%2 == 0) and (row_text.find('No Record Found') == -1):
            td_counter=0
            
            #source
            print('Source               :', sources[dep-1])

            tds=row.find_elements(By.TAG_NAME,'td')
            
            '''
            #caculating total no. of td(s)
            total_td=0
            for z in tds:
                total_td+=1
            '''

            for td in tds:
                
                td_counter+=1

                #appeal number and month/year
                if td_counter==2:
                    temp=[]
                    temp.append(td.text)
                    print('Case id              :', temp[0])
                    print('Month/Year           :', current_day.strftime('%m/%Y'))
                    #case.case_id = temp[0]
                    #case.year = current_day.strftime('%Y')


                #title and pdf link
                if td_counter==4:
                    temp=[]
                    temp.append(td.text)
                    print('Title                :', temp[0])


                    a_tags=td.find_elements(By.TAG_NAME, 'a')
                    for a_tag in a_tags:
                        print('pdf link             :', a_tag.get_attribute('href'))
                        pdf_link=a_tag.get_attribute('href')
                        #case.url=pdf_link
                        #judgement_txt=extract_txt(pdf_link, 'Court_Extract.pdf')
                        #case.judgement_text=judgement_txt
            
            #spacing b/w judgemnets
            print()

            #processing all the extracted data
            #case.process_text()
            #case.print_case_attributes()
            #store_case_document(case)    

    
    #back to main page
    driver.back()
    driver.back()


#closing the chrome instance/window
driver.quit()