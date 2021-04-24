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


def nclt_jud_scrapper(bench_name):
    #scrapping page's data
    case=CaseDoc()
    
    #loacting target table for scrapping
    table=driver.find_element_by_xpath('//*[@id="block-system-main"]/div/div/div[1]/table')
    t_body=table.find_element_by_tag_name('tbody')
    rows=t_body.find_elements(By.TAG_NAME,'tr')
    
    row_counter=0
    for row in rows:
        row_counter+=1

        if row_counter>0:

            td_counter=0
            
            tds=row.find_elements(By.TAG_NAME,'td')
            

            #bench name and source
            #print('Bench                   :', bench_name)
            case.bench = bench_name
            case.source = 'National Company Law Tribunal'


            for td in tds:
                td_counter+=1

                #case number --> Diary No. 
                if td_counter==2:
                    temp=[]
                    temp.append(td.text)
                    #print('Case id                 :', temp[0])
                    case.case_id = temp[0]


                #petitioner & respondent
                if td_counter==3:
                    temp=[]
                    temp.append(td.text)
                    temp_str=temp[0]
                    slice_1=temp_str.find('Vs')
                    #slice_2=temp_str.find('\n')
                    slice_3=temp_str.find('Respondent Advocate')
                    #print(temp)
                    #print('Petitioner              :', temp_str[0:slice_1])
                    #print('Respondent              :', temp_str[slice_1+3:slice_3-1])
                    #print('Respondent Advocate     :', temp_str[slice_2+1:slice_3-1])
                    case.petitioner = temp_str[0:slice_1]
                    case.respondent = temp_str[slice_1+3:slice_3-1]


                #date of judgement
                if td_counter==4:
                    temp=[]
                    temp.append(td.text)
                    #print('Date of Judgement       :', temp[0])
                                            
                    date=datefinder.find_dates(temp[0])
                    for i in date:
                        date=i 
                    case.date=date
                    case.year = date.strftime("%Y")
                    
                
                #pdf link
                if td_counter==5:
                    a_tags = td.find_elements(By.TAG_NAME,"a")
                    for a_tag in a_tags:
                        #print('Pdf link                :', a_tag.get_attribute('href'))
                        pdf_link=a_tag.get_attribute('href')
                        case.url=pdf_link
                        judgement_txt=extract_txt(pdf_link, 'Court_Extract.pdf')
                        case.judgement_text=judgement_txt
                        
            #spacing b/w judgemnets
            print()            

            #processing all the extracted data
            case.process_text()
            case.print_case_attributes()
            #store_case_document(case)
                
      



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
driver.get('https://nclt.gov.in/exposed-judgement-date-wise-page')
time.sleep(1)

'''
#judgements --> judgement date wise
driver.find_element_by_xpath('//*[@id="navbarResponsive"]/ul/li[4]/a').click()
driver.find_element_by_xpath('//*[@id="node-297045"]/div/div/div/div/ul/li[1]/a').click()
time.sleep(1)
'''
#setting start/end date- (past 1 week)
current_day=datetime.date.today()
week_control=current_day-datetime.timedelta(days=90)
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
for benches in range(2,4):

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

                #bench name and source
                #('Bench                   :', bench_name)
                case.bench = bench_name
                case.source = 'National Company Law Tribunal'


                for td in tds:
                    td_counter+=1

                    #case number --> Diary No. 
                    if td_counter==2:
                        temp=[]
                        temp.append(td.text)
                        #print('Case id                 :', temp[0])
                        case.case_id = temp[0]


                    #petitioner & respondent
                    if td_counter==3:
                        temp=[]
                        temp.append(td.text)
                        temp_str=temp[0]
                        slice_1=temp_str.find('Vs')
                        #slice_2=temp_str.find('\n')
                        slice_3=temp_str.find('Respondent Advocate')
                        #print(temp)
                        #print('Petitioner              :', temp_str[0:slice_1])
                        #print('Respondent              :', temp_str[slice_1+3:slice_3-1])
                        #print('Respondent Advocate     :', temp_str[slice_2+1:slice_3-1])
                        case.petitioner = temp_str[0:slice_1]
                        case.respondent = temp_str[slice_1+3:slice_3-1]


                    #date of judgement
                    if td_counter==4:
                        temp=[]
                        temp.append(td.text)
                        #print('Date of Judgement       :', temp[0])
                                                
                        date=datefinder.find_dates(temp[0])
                        for i in date:
                            date=i 
                        case.date=date
                        case.year = date.strftime("%Y")
                        
                    
                    #pdf link
                    if td_counter==5:
                        a_tags = td.find_elements(By.TAG_NAME,"a")
                        for a_tag in a_tags:
                            #print('Pdf link                :', a_tag.get_attribute('href'))
                            pdf_link=a_tag.get_attribute('href')
                            case.url=pdf_link
                            judgement_txt=extract_txt(pdf_link, 'Court_Extract.pdf')
                            case.judgement_text=judgement_txt
                            
                #spacing b/w judgemnets
                #print()            

                #processing all the extracted data
                case.process_text()
                case.print_case_attributes()
                #store_case_document(case)


        #code for accessing next pages
        # will access 2nd last li tag (next) to go to the next page

        #calculating total no. of li tags(lis, li_counter) 
        ul=driver.find_element_by_xpath('//*[@id="block-system-main"]/div/div/div[2]/ul')        
        lis=ul.find_elements(By.TAG_NAME, 'li')
        li_counter=0
        for li in lis:
            li_counter+=1

        second_last_li_index = li_counter-1  

        k= True
        nxt_pg_counter=0

        while k:               
            if (driver.find_element_by_xpath('//*[@id="block-system-main"]/div/div/div[2]/ul/li[{next_index}]/a'.format(next_index=second_last_li_index)) and (driver.find_element_by_xpath('//*[@id="block-system-main"]/div/div/div[2]/ul/li[{next_index}]/a'.format(next_index=second_last_li_index)).text == 'next ›')): 
                nxt_pg_counter+=1
                driver.find_element_by_xpath('//*[@id="block-system-main"]/div/div/div[2]/ul/li[{next_index}]/a'.format(next_index=second_last_li_index)).click()
                
                #for countering first/prev li tags
                #calculating second_last_li_index for new pg
                ul=driver.find_element_by_xpath('//*[@id="block-system-main"]/div/div/div[2]/ul')        
                lis=ul.find_elements(By.TAG_NAME, 'li')
                li_counter=0
                for li in lis:
                    li_counter+=1

                second_last_li_index = li_counter-1
                
                #calling scrapper
                nclt_jud_scrapper(bench_name)
                time.sleep(2)

            else:
                k=False
                #print('going back to pg-1')
                driver.execute_script('window.history.go({0})'.format(-(nxt_pg_counter)))
                time.sleep(1)
                
        #back to bench selection page
        #print('going back to bench selection pg')
        driver.back()

    except:
        #back to bench selection page
        #print('going back to bench selection pg--')
        driver.back()

#closing chrome istance/window
driver.quit()