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


#opening an instance @compatarchives.nclat.nic.in/Judgements.aspx
driver.get('http://compatarchives.nclat.nic.in/Judgements.aspx')
time.sleep(1)

#choosing 100 enteries view at a time from drop down menu
driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_gvJudgement_length"]/label/select').click()
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_gvJudgement_length"]/label/select/option[4]').click()
time.sleep(1)


#scrapping page's data
case=CaseDoc()


#calculating counter for loop
#(-2) for excluding 'previous' and 'next' page li tags
counter=-2
ul=driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_gvJudgement_paginate"]/ul')

#finding li tags under the ul tag
lis=ul.find_elements(By.TAG_NAME, 'li')

for li in lis:
    counter+=1
#print(counter)


for x in range(counter):

    #loacting target table for scrapping
    table=driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_gvJudgement"]')
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

        #counter for td tags
        td_counter=0

        #accessing td tags of each row(tr tag)
        tds=row.find_elements(By.TAG_NAME,'td')
        
        '''
        #caculating total no. of td(s) tags inside each tr tag
        total_td=0
        for z in tds:
            total_td+=1
        '''

        for td in tds:
            td_counter+=1

            #case number --> Appeal No. (with IA No.<optional>) 
            if td_counter==2:
                temp=[]
                temp.append(td.text)
                print('Case id                     :', temp[0])

                #case.case_id = temp[0]

            
            #Petitioner (Appellants)
            if td_counter==3:
                temp=[]
                temp.append(td.text)
                print('Petitioner                  :', temp[0])
                
                #case.petitioner = temp[0]


            #Respondents
            if td_counter==4:
                temp=[]
                temp.append(td.text)
                print('Respondent                  :', temp[0])

                #case.respondent = temp[0]


            #date of judgement
            if td_counter==5:
                temp=[]
                temp.append(td.text)
                print('Date of Judgement           :', temp[0])
                
                
                date=datefinder.find_dates(temp[0])
                for i in date:
                    date=i 
                #print(date)
                
                #case.date=date
                #case.year = date.strftime("%Y")
                

            #Member/judge
            if td_counter==6:
                temp=[]
                temp.append(td.text)
                print('Bench                       :', temp[0])

                #case.bench = temp[0]
                #case.source = 'Telecom Disputes Settlement and Appellate Tribunal'



            #pdf link
            if td_counter==7:
                a_tags = td.find_elements(By.TAG_NAME,"a")
                for a_tag in a_tags:
                    #print('Pdf link                    :', a_tag.get_attribute('href'))
                    #pdf_link=a_tag.get_attribute('href')
                    
                    pdf = a_tag.click()
                    print(pdf)

                    #case.url=pdf_link
                    #judgement_text=extract_txt(pdf_link, 'Court_Extract.pdf')
                    #case.judgement_text=judgement_txt
   
                            
        #spacing b/w judgemnets
        print()

        #processing all the extracted data
        #case.process_text()
        #case.print_case_attributes()
        #store_case_document(case)


    #searching next button if present then continue loop otherwise exit the loop
    try:
        driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_gvJudgement_next"]/a').click()
        time.sleep(1)

    except:
        print('Exception Occured!!!')
        break
    

#closing chrome instance/window
driver.close()