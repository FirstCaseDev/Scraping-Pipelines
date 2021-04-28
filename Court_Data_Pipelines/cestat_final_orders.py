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

#opening an instance @https://cestatnew.gov.in --> final orders
driver.get('https://cestatnew.gov.in/')
time.sleep(1)

#saving window'index name using window handle
home_pg = driver.window_handles[0]

driver.find_element_by_xpath('//*[@id="v_navcontainer"]/ul/li[6]/a').click()
time.sleep(1)

#saving window'index name using window handle
final_orders_pg = driver.window_handles[1]
#new seperate window opens
#accessing final orders pg window
driver.switch_to_window(final_orders_pg) 


#chosen filter --> date wise
#setting start/end date- (past 1 week)
current_day=datetime.date.today()
week_control=current_day-datetime.timedelta(days=28)
from_date=week_control.strftime('%Y-%m-%d')


#curretnt date
to_date=datetime.date.today().strftime('%Y-%m-%d')

#filling the dates
from_day_box = driver.find_element_by_xpath('/html/body/fieldset[3]/table/tbody/tr/td[1]/input')
from_day_box.send_keys(from_date)

to_day_box = driver.find_element_by_xpath('/html/body/fieldset[3]/table/tbody/tr/td[2]/input')
to_day_box.send_keys(to_date)

#go button
go=driver.find_element_by_xpath('/html/body/fieldset[3]/table/tbody/tr/td[3]/input').click()
time.sleep(3)                   

#scrapping page's data
case=CaseDoc()

try:
    #loacting target table for scrapping
    table=driver.find_element_by_xpath('/html/body/table[7]')
    t_body=table.find_element_by_tag_name('tbody')
    rows=t_body.find_elements(By.TAG_NAME,'tr')
    
    row_counter=0
    
    #coumting total no. of rows
    total_rows=0
    for x in rows:
        total_rows+=1
        
    for row in rows:

        row_counter+=1

        if row_counter>1:

            td_counter=0

            tds=row.find_elements(By.TAG_NAME,'td')
            
            for td in tds:
                td_counter+=1

                #case-id 
                if td_counter==2:
                    temp=[]
                    temp.append(td.text)
                    print('Case id              :', temp[0][2:])
                    #case.case_id=temp[0]


                #petitioner & respondent
                if td_counter==3:
                    temp=[]
                    temp.append(td.text)
                    temp_str=temp[0]
                    slice_1=temp_str.find('---VS.---')
                    #print(temp)
                    print('Petitioner           :', temp_str[0:slice_1-1])
                    print('Respondent           :', temp_str[slice_1+10:])
                    #case.petitioner = temp_str[0:slice_1-1]
                    #case.respondent = temp_str[slice_1+10:]   


                #order date (dd/mm/yyyy)
                if td_counter==5:
                    temp=[]
                    temp.append(td.text)
                    print('Date of Order        :', temp[0])
                                                
                    date=datefinder.find_dates(temp[0])
                    for i in date:
                        date=i 
                    #case.date=date
                    #case.year = date.strftime("%Y")


                #pdf link
                if td_counter==7:
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


    #closing the final orders window when scrapping gets completed
    driver.close()

except:
    #closing the final orders window if no data is found
    #print('exception occurred :')
    driver.close()

#switching back to home page
driver.switch_to_window(home_pg)
driver.close()