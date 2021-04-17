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

#opening an instance @CULCUTTA.GOV.IN
driver.get('https://www.calcuttahighcourt.gov.in/Order-Judgments')
time.sleep(1)


#setting start/end date- (past 1 week)
current_day=datetime.date.today()
week_control=current_day-datetime.timedelta(days=56)

from_date=week_control.strftime('%d-%b-%Y')
#format 15-Apr-2021
#print(from_date)

#curretnt date
to_date=datetime.date.today().strftime('%d-%b-%Y')
#print(to_date)


#filling from/to date 
from_date_box=driver.find_element_by_xpath('//*[@id="order_from_date"]')
#to delete default text
back=Keys.BACK_SPACE
for x in range(11):
    from_date_box.send_keys(back)

from_date_box.send_keys(from_date)

to_date_box=driver.find_element_by_xpath('//*[@id="order_to_date"]')
to_date_box.send_keys(to_date)


#clicking search button
driver.find_element_by_xpath('//*[@id="search-button"]').click()
time.sleep(5)

#scrapping page's data
case=CaseDoc()

while True:
    #load more
    try:
        load_more=driver.find_element_by_xpath('//*[@id="load_more"]')
        load_more.click()
        time.sleep(3)
    except:
        time.sleep(1)
        break


#loacting target table for scrapping
table=driver.find_element_by_xpath('//*[@id="datatable-table"]')
t_body=table.find_element_by_tag_name('tbody')

rows=t_body.find_elements(By.TAG_NAME,'tr')

tr_counter=0

for row in rows:
    tr_counter+=1
    #print(tr_counter)

    tds=row.find_elements(By.TAG_NAME, 'td')
    td_counter=0

    for td in tds:
        
        td_counter+=1
        
        #case number and pdf link
        if td_counter==2:
            #caes no.
            temp=[]
            temp.append(td.text)
            print('Case id          :', temp[0])
            #case.case_id=temp[0]

            #pdf_link
            a_tags=td.find_elements(By.TAG_NAME,'a')

            for a_tag in a_tags:
                pdf_link=a_tag.get_attribute('href')
                print('Pdf link         :', pdf_link)
                #case.url=pdf_link
                #judgement_txt=extract_txt(pdf_link, 'Court_Extract.pdf')
                #case.judgement_text=judgement_txt


        #skipping judges    td_counter==3
        #skipping order     td_counter==4


        #date of judgement
        if td_counter==5:
            temp=[]
            temp.append(td.text)
            jud_date=temp[0]
            print('Date             :', jud_date)

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

        
        
        




