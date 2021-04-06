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
client = pymongo.MongoClient("mongodb+srv://PuneetShrivas:admin@betatesting.nsnxl.mongodb.net/<dbname>?retryWrites=true&w=majority")
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

#opening an instance @NCLT.GOV.IN
driver.get('https://nclt.gov.in/')
time.sleep(1)

#judgements --> judgement date wise
driver.find_element_by_xpath('//*[@id="navbarResponsive"]/ul/li[4]/a').click()
driver.find_element_by_xpath('//*[@id="node-297045"]/div/div/div/div/ul/li[1]/a').click()
time.sleep(1)

#setting start/end date- (past 1 week)
current_day=datetime.date.today()
week_control=current_day-datetime.timedelta(days=7)
start_date=week_control.strftime('%d/%m/%Y')
temp=start_date[:-4]+start_date[-2:]
#print(temp)
start_date=temp


#curretnt date
end_date=datetime.date.today().strftime('%d/%m/%Y')
temp=end_date[:-4]+end_date[-2:]
#print(temp)
end_date=temp

#filling the dates
start_day_box = driver.find_element_by_xpath('//*[@id="edit-field-search-date-value-min-datepicker-popup-0"]')
start_day_box.send_keys(start_date)

end_day_box = driver.find_element_by_xpath('//*[@id="edit-field-search-date-value-max-datepicker-popup-0"]')
end_day_box.send_keys(end_date)


#loop for diffrent benches(21 in total)
for benches in range(2,23):

    #accessing final judgements --> Bench wise
    driver.find_element_by_xpath('//*[@id="edit-field-bench-target-id"]').click()
    driver.find_element_by_xpath('//*[@id="edit-field-bench-target-id"]/option[{bench_index}]'.format(bench_index=benches)).click()
    bench_name=driver.find_element_by_xpath('//*[@id="edit-field-bench-target-id"]/option[{bench_index}]'.format(bench_index=benches)).text
    time.sleep(1)
    
    #display button
    driver.find_element_by_xpath('//*[@id="front-Compare-button-new-1"]').click()


    #scrapping page's data
    case=CaseDoc()
    #loacting target table for scrapping
    try:
        table=driver.find_element_by_xpath('//*[@id="block-system-main"]/div/div/div[1]/table')
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

            if row_counter>0:

                td_counter=0
                
                tds=row.find_elements(By.TAG_NAME,'td')
                
                '''
                #caculating total no. of td(s)
                total_td=0
                for z in tds:
                    total_td+=1
                '''
                #bench name
                print('Bench                   :', bench_name)

                for td in tds:
                    td_counter+=1

                    #case number --> Diary No. 
                    if td_counter==2:
                        temp=[]
                        temp.append(td.text)
                        print('Case id                 :', temp[0])

                    #petitioner & respondent
                    if td_counter==3:
                        temp=[]
                        temp.append(td.text)
                        temp_str=temp[0]
                        slice_1=temp_str.find(' Vs ')
                        slice_2=temp_str.find('\n')
                        slice_3=temp_str.find('Respondent Advocate')
                        #print(temp)
                        print('Petitioner              :', temp_str[0:slice_1])
                        print('Respondent              :', temp_str[slice_1+4:slice_2])
                        #print('Respondent Advocate     :', temp_str[slice_2+1:slice_3-1])


                    #date of judgement
                    if td_counter==4:
                        temp=[]
                        temp.append(td.text)
                        print('Date of Judgement       :', temp[0])
                                                
                        date=datefinder.find_dates(temp[0])
                        for i in date:
                            date=i 
                        case.date=date
                        case.year = date.strftime("%Y")
                        
                    
                    #pdf link
                    if td_counter==5:
                        a_tags = td.find_elements(By.TAG_NAME,"a")
                        for a_tag in a_tags:
                            print('Pdf link                :', a_tag.get_attribute('href'))
                
                #spacing b/w judgemnets
                print()            
        
        #back to bench selection page
        driver.back()

    except:
        driver.back()

#closing chrome istance/window
driver.quit()

