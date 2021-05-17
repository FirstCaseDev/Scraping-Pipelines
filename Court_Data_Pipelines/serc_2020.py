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


#opening an instance @www.cercind.gov.in/recent_orders2020.html
driver.get('http://www.cercind.gov.in/recent_orders2020.html')
time.sleep(1)

#scrapping page's data
case=CaseDoc()

try:
    #loacting target table for scrapping
    table=driver.find_element_by_xpath('/html/body/section/div/div/div/div/table')
    t_body=table.find_element_by_tag_name('tbody')
    rows=t_body.find_elements(By.TAG_NAME,'tr')

    
    
    #coumting total no. of rows
    total_rows=0
    for x in rows:
        total_rows+=1
    

    #counter for tr tags
    row_counter=0

    for row in rows:

        row_counter+=1
        
        if (row_counter>=2):
            #counter for td tags
            td_counter=0
            
            tds=row.find_elements(By.TAG_NAME,'td')
            
            '''
            #caculating total no. of td(s)
            total_td=0
            for z in tds:
                total_td+=1
            '''

            for td in tds:
                
                td_counter+=1

                #case number --> petition number 
                if td_counter==1:
                    temp=[]
                    temp.append(td.text)
                    print('Case id               :', temp[0])
                    #case.case_id=temp[0]


                #Subject and pdf link
                if td_counter==2:
                    print('Description           :', td.text)
                    a_tags = td.find_elements(By.TAG_NAME,"a")
                    for a_tag in a_tags:
                        print('Pdf link              :', a_tag.get_attribute('href'))
                        #case.url=pdf_link
                        #judgement_txt=extract_txt(pdf_link, 'Court_Extract.pdf')
                        #case.judgement_text=judgement_txt

                #date of order -->dd.mm.yyyy
                if td_counter==3:
                    temp=[]
                    temp.append(td.text)
                    print('Date of Order         :', temp[0])
                                                
                    date=datefinder.find_dates(temp[0])
                    for i in date:
                        date=i 
                    #case.date=date
                    #case.year = date.strftime("%Y")
                                  

                #skipping upload date for td_counter=4


                #category
                if td_counter==5:
                    print("Category              :", td.text)
            
            #spacing b/w judgemnets
            print()

            #processing all the extracted data
            #case.process_text()
            #case.print_case_attributes()
            #store_case_document(case) 

except:
    print('Exception occurred!!!')           

#print(total_rows, row_counter)

#closing the chrome instance/window
driver.quit()