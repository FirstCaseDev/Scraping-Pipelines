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

#opening an instance @https://www.ipab.gov.in/order_chennai_pt.php
driver.get('https://www.ipab.gov.in/order_chennai_pt.php')
time.sleep(1)


cities= ['chennai', 'delhi', 'mumbai', 'kolkata', 'ahmedabad']

#scrapping page's data
case=CaseDoc()

bench_counter=0

#loop for benches --> format -->//*[@id="chennai"]
for bench in cities:

    bench_counter+=1
    print('Bench Name           :', bench.upper())

    #loop for sub-categories --> Tm, patents, etc.
    for sub_cat in range(1,6):

        #accessing the becnh drop-down list
        driver.find_element_by_xpath('//*[@id="{bench_index}"]'.format(bench_index = bench)).click()
        time.sleep(1)

        #accessing sub-categories
        sub = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/div/div/div[2]/div[{div_index}]/ul/li[{sub_cat_index}]/a'.format(div_index = bench_counter + 1, sub_cat_index = sub_cat))
        sub.click()                         
        time.sleep(1)

        #loacting target table for scrapping
        table=driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[2]/div/div/table')
        t_body=table.find_element_by_tag_name('tbody')
        rows=t_body.find_elements(By.TAG_NAME,'tr')
        
        '''
        #row_counter=0
        #coumting total no. of rows
        total_rows=0
        for x in rows:
            total_rows+=1
        '''

        for row in rows:

            #row_counter+=1
            if (row.text != 'This page will be updated soon') :

                td_counter=0

                tds=row.find_elements(By.TAG_NAME,'td')
                
                for td in tds:
                    td_counter+=1

                    #application number
                    if td_counter==1:
                        temp=[]
                        temp.append(td.text)
                        print('Case id              :', temp[0])
                        #case.case_id=temp[0]


                    #order date (dd-mm-yyyy)
                    if td_counter==2:
                        temp=[]
                        temp.append(td.text)
                        print('Date of Order        :', temp[0])
                                                    
                        date=datefinder.find_dates(temp[0])
                        for i in date:
                            date=i 
                        #case.date=date
                        #case.year = date.strftime("%Y")
                                        
                    #td_counter==3 --> coram

                    #petitioner 
                    if td_counter==4:
                        temp=[]
                        temp.append(td.text)
                        temp_str=temp[0]
                        #print(temp)
                        print('Petitioner           :', temp_str)
                        #case.petitioner = temp_str

                    #Respondent
                    if td_counter==5:
                        temp=[]
                        temp.append(td.text)
                        temp_str=temp[0]
                        print('Respondent           :', temp_str)
                        #case.respondent = temp_str


                    #pdf link
                    if td_counter==6:
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



#closing chrome istance/window
driver.quit()