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

#opening an instance @www.itat.gov.in/judicial/tribunalorders
driver.get('https://www.itat.gov.in/judicial/tribunalorders')
time.sleep(1)


#for 31 benches
for x in range(31):

    driver.find_element_by_xpath('//*[@id="bench"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="bench"]/option[{bench_index}]'.format(bench_index=x+2)).click()

    bench_name=driver.find_element_by_xpath('//*[@id="bench"]/option[{bench_index}]'.format(bench_index=x+2)).text
    print(bench_name)
    
    '''
    #date
    date_box=driver.find_element_by_xpath('//*[@id="orderdate"]')
    date=datetime.date.today().strftime('%d/%m/%Y')
    date_box.send_keys(date)
    '''

    #search button
    driver.find_element_by_xpath('//*[@id="tribunalOrder"]/table/tbody/tr[4]/td[4]/button[1]').click()
    time.sleep(1)

    try:

        #loacting target table for scrapping
        table=driver.find_element_by_xpath('//*[@id="content"]/div/table')
        t_body=table.find_element_by_tag_name('tbody')
        rows=t_body.find_elements(By.TAG_NAME,'tr')
        
        row_counter=0
        
        #counting total no. of rows
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

                    #case-id (Appeal number)
                    if td_counter==1:
                        temp=[]
                        temp.append(td.text)
                        print('Case id              :', temp[0])

                        #case.case_id=temp[0]


                    #petitioner (appellant)  respondent
                    if td_counter==3:
                        temp=[]
                        temp.append(td.text)                        
                        print('Petitioner           :', temp[0])
                        
                        #case.petitioner = temp[0]
                        
                    
                    #respondent
                    if td_counter==4:
                        temp=[]
                        temp.append(td.text)                        
                        print('Respondent           :', temp[0])
                        
                        #case.respondent = temp[0]   


                    #details
                    if td_counter==5:
                        
                        #saving main page window's index name using window handle
                        main_pg = driver.window_handles[0]
                        
                        td.click()
                        time.sleep(1)

                        #saving detail page's 
                        detail_pg = driver.window_handles[1]

                        #accessing detail pg window
                        driver.switch_to_window(detail_pg) 
                        
                        try:

                            #loacting target table for scrapping
                            table=driver.find_element_by_xpath('//*[@id="showhide"]/div/main/div/div/div/section[5]/div/table')
                            t_body=table.find_element_by_tag_name('tbody')
                            rows=t_body.find_elements(By.TAG_NAME,'tr')
                            
                            row_counter=0
                            
                            #counting total no. of rows
                            total_rows=0
                            for x in rows:
                                total_rows+=1
                                
                            for row in rows:

                                row_counter+=1

                                if row_counter==2:

                                    td_counter=0

                                    tds=row.find_elements(By.TAG_NAME,'td')
                                    
                                    for td in tds:
                                        td_counter+=1

                                        #order date (dd/mm/yyyy)
                                        if td_counter==2:
                                            temp=[]
                                            temp.append(td.text)
                                            print('Date of Order        :', temp[0])
                                                                        
                                            date=datefinder.find_dates(temp[0])
                                            for i in date:
                                                date=i 
                                            #case.date=date
                                            #case.year = date.strftime("%Y")
                                                                                    

                                        #pdf link
                                        if td_counter==6:
                                            a_tags=td.find_elements(By.TAG_NAME, 'a')
                                            for a_tag in a_tags:
                                                print('pdf link             :', a_tag.get_attribute('href'))
                                                pdf_link=a_tag.get_attribute('href')
                                                #case.url=pdf_link
                                                #judgement_txt=extract_txt(pdf_link, 'Court_Extract.pdf')
                                                #case.judgement_text=judgement_txt
                        except:
                            print('Exception at details page')

                        #closing details page
                        #switching back to main page
                        driver.close()
                        driver.switch_to_window(main_pg)        

                #spacing b/w judgemnets
                print()

                #processing all the extracted data
                #case.process_text()
                #case.print_case_attributes()
                #store_case_document(case)

       
    except:  
        print('No Data Available')
        
        #reset button
        driver.find_element_by_xpath('//*[@id="tribunalOrder"]/table/tbody/tr[4]/td[4]/button[2]').click()
        
        continue

    #reset button
    driver.find_element_by_xpath('//*[@id="tribunalOrder"]/table/tbody/tr[4]/td[4]/button[2]').click()

#closing chrome instance/window
driver.close()