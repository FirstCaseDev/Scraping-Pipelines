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
driver.get('https://nclat.nic.in/?page_id=123#')
time.sleep(1)


#judgement date section
driver.find_element_by_xpath('//*[@id="exTab1"]/ul/li[2]/a').click()
time.sleep(1)


#setting start/end date- (past 1 week)
current_day=datetime.date.today()
week_control=current_day-datetime.timedelta(days=7)
start_date=week_control.strftime('%m/%d/%Y')


#curretnt date
end_date=datetime.date.today().strftime('%m/%d/%Y')

#filling the dates
start_day_box = driver.find_element_by_xpath('//*[@id="from_date"]')
start_day_box.send_keys(start_date)

end_day_box = driver.find_element_by_xpath('//*[@id="to_date"]')
end_day_box.send_keys(end_date)


#loop for diffrent benches(6 in total)
for benches in range(2,8):

    #accessing judgements --> Bench wise
    driver.find_element_by_xpath('//*[@id="court"]').click()
    driver.find_element_by_xpath('//*[@id="court"]/option[{bench_index}]'.format(bench_index=benches)).click()
    
    #search button
    driver.find_element_by_xpath('//*[@id="judfilter"]').click()
    time.sleep(2)

    #scrapping page's data
    case=CaseDoc()
    #loacting target table for scrapping
    try:
        table=driver.find_element_by_xpath('//*[@id="order_table"]/div/div[2]/table')
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
            #row_counter+=1
        
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

                #case number --> Company appeal/ AT No. 
                if td_counter==1:
                    temp=[]
                    temp.append(td.text)
                    if td.text != 'No Record Found':
                        print('Case id                     :', temp[0])
                        case.case_id = temp[0]
                                    
                #date of judgement
                if td_counter==2:
                    temp=[]
                    temp.append(td.text)
                    print('Date of Judgement           :', temp[0])
                    
                    
                    date=datefinder.find_dates(temp[0])
                    for i in date:
                        date=i 
                    case.date=date
                    case.year = date.strftime("%Y")
                    
                
                #petitioner & respondent
                if td_counter==3:
                    temp=[]
                    temp.append(td.text)
                    temp_str=temp[0]
                    slice_1=temp_str.find(' VS ')
                    #print(temp)
                    print('Petitioner                  :', temp_str[0:slice_1])
                    print('Respondent                  :', temp_str[slice_1+4:])

                    #case.petitioner = temp_str[0:slice_1]
                    #case.respondent = temp_str[slice_1+4:]

                #skipping section (td_counter==4)

                #Bench name
                if td_counter==5:
                    temp=[]
                    temp.append(td.text)
                    print('Bench                       :', temp[0])

                    #case.source = 'NATIONAL COMPANY LAW APPELLATE TRIBUNAL'                    


                #judges 
                if td_counter==6:
                    temp=[]
                    temp.append(td.text)
                    judges=temp[0]
                    print('Judge(s)                     :', judges)

                    #case.bench=judges

                #pdf link
                if td_counter==7:
                    a_tags = td.find_elements(By.TAG_NAME,"a")
                    for a_tag in a_tags:
                        print('Pdf link                    :', a_tag.get_attribute('href'))
                        pdf_link=a_tag.get_attribute('href')
                        #case.url=pdf_link
                        #judgement_txt=extract_txt(pdf_link, 'Court_Extract.pdf')
                        #case.judgement_text=judgement_txt

                #skipping remark (td_counter==8)
                                
            #spacing b/w judgemnets
            print()

            #processing all the extracted data
            #case.process_text()
            #case.print_case_attributes()
            #store_case_document(case)

    except:
        continue

#closing chrome istance/window
driver.quit()








