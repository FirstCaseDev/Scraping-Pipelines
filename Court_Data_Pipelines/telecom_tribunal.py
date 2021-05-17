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


#opening an instance @tdsat.gov.in/Delhi/services/judgment.php
driver.get('https://tdsat.gov.in/Delhi/services/judgment.php')
time.sleep(1)

#setting start/end date- (past 5 months)
current_day=datetime.date.today()
week_control=current_day-datetime.timedelta(days=150)
from_date=week_control.strftime('%d/%m/%Y')

#curretnt date
to_date=datetime.date.today().strftime('%d/%m/%Y')

#filling the dates
from_day_box = driver.find_element_by_xpath('//*[@id="mydate"]')
driver.execute_script('document.getElementsByName("from_date1")[0].removeAttribute("readonly")')
#from_day_box.click()
from_day_box.send_keys(from_date)

to_day_box = driver.find_element_by_xpath('//*[@id="mydate1"]')
driver.execute_script('document.getElementsByName("to_date1")[0].removeAttribute("readonly")')
#to_day_box.click()
to_day_box.send_keys(to_date)

#go button
driver.find_element_by_xpath('//*[@id="submit1"]').click()
time.sleep(1)


#scrapping page's data
case=CaseDoc()

try:

    #loacting target table for scrapping
    table=driver.find_element_by_xpath('/html/body/form[3]/fieldset/div/table')
    t_body=table.find_element_by_tag_name('tbody')

    rows=t_body.find_elements(By.TAG_NAME,'tr')

    row_counter=0
    total_rows=0

    #counting total no. of rows
    for row in rows:
        total_rows+=1

    #traversing through rows of the table
    for row in rows:
        
        row_counter+=1

        td_counter=0

        tds=row.find_elements(By.TAG_NAME,'td')
        
        '''
        #caculating total no. of td(s) tags inside each tr 
        total_td=0
        for z in tds:
            total_td+=1
        '''

        for td in tds:
            td_counter+=1

            #case number --> Company appeal/ AT No. 
            if td_counter==2:
                temp=[]
                temp.append(td.text)
                print('Case id                     :', temp[0])

                #case.case_id = temp[0]


            #Member/judge
            if td_counter==3:
                temp=[]
                temp.append(td.text)
                print('Bench                       :', temp[0])

                #case.bench = temp[0]
                #case.source = 'Telecom Disputes Settlement and Appellate Tribunal'


            #petitioner & respondent(Party Detail)
            if td_counter==4:
                temp=[]
                temp.append(td.text)
                temp_str=temp[0]
                
                l=temp_str.split('VS')
                #print(l)

                print('Petitioner                  :', l[0][:-1])
                print('Respondent                  :', l[-1][1:])
                #case.petitioner = l[0][:-1]
                #case.respondent = l[-1][1:]


            #date of judgement
            if td_counter==5:
                temp=[]
                temp.append(td.text)
                print('Date of Judgement           :', temp[0])
                
                
                date=datefinder.find_dates(temp[0])
                for i in date:
                    date=i 

                #case.date=date
                #case.year = date.strftime("%Y")
                


            #pdf link
            if td_counter==6:
                a_tags = td.find_elements(By.TAG_NAME,"a")
                for a_tag in a_tags:
                    print('Pdf link                    :', a_tag.get_attribute('href'))
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

except:
    print('No data found')
    driver.close()

#closing chrome instance/window
driver.close()