from selenium import webdriver
import time
import datetime
import datefinder
import pymongo
#from Common_Files.Case_pdf_handling import extract_txt
#from Common_Files.Case_storage import store_case_document, case_exists_by_case_id
#from Common_Files.Case_handler import CaseDoc 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located

'''
#accessing Case_storage database
client = pymongo.MongoClient("mongodb+srv://PuneetShrivas:admin@betatesting.nsnxl.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client["indian_court_data"]
col = db["cases"]
'''

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

#opening an instance @NCLT
driver.get('http://164.100.158.181/default.htm')
time.sleep(1)

#loop for diffrent benches(12 in total)
for benches in range(1,13):
    #accessing final orders --> Bench wise
    driver.find_element_by_xpath('//*[@id="top_menu"]/ul/li[4]/a').click()
    bench_name=driver.find_element_by_xpath('//*[@id="top_menu"]/ul/li[4]/ul/li[{bench_index}]/a'.format(bench_index=benches)).text
    driver.find_element_by_xpath('//*[@id="top_menu"]/ul/li[4]/ul/li[{bench_index}]/a'.format(bench_index=benches)).click()
    time.sleep(2)
    #bench_name=driver.find_element_by_xpath('//*[@id="skip"]/div/div[2]/ul/li[5]/ul/li[{bench_index}]/a'.format(bench_index=benches)).text
    #//*[@id="skip"]/div/div[2]/ul/li[5]/ul/li[1]/a
    #//*[@id="top_menu"]/ul/li[4]/ul/li[1]/a
    time.sleep(1)


    #loop for differnt years(2016,2017,2018)
    for years in range(2,5):
        
        #loop for different sections(111-111 A/ 58-59, 397-398/ 241-242, Others)
        for sections in range(2,5):

            #selecting years
            driver.find_element_by_xpath('//*[@id="year"]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="year"]/option[{year_index}]'.format(year_index=years)).click()

            #selecting sections
            driver.find_element_by_xpath('//*[@id="section"]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="section"]/option[{section_index}]'.format(section_index=sections)).click()

            #clicking go button
            driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[3]/input').click()
            time.sleep(2)

            #waiting to load all elements of the present table
            WebDriverWait(driver,10).until(presence_of_all_elements_located((By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/table')))
            
            
            #scrapping page's data
            
            #case=CaseDoc()
            #loacting target table for scrapping
            table=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/table')
            t_body=table.find_element_by_tag_name('tbody')

            rows=t_body.find_elements(By.TAG_NAME,'tr')

            row_counter=0
            
            '''
            #coumting total no. of rows
            total_rows=0
            for x in rows:
                total_rows+=1
            '''

            for row in rows:
                row_counter+=1

                if row_counter>1:

                    td_counter=0
                                        
                    tds=row.find_elements(By.TAG_NAME,'td')
                    
                    '''
                    #caculating total no. of td(s)
                    total_td=0
                    for z in tds:
                        total_td+=1
                    '''
                    
                    #bench name
                    print('Bench                 :', bench_name)

                    for td in tds:
                        td_counter+=1

                        #case number --> CP No. 
                        if td_counter==1:
                            temp=[]
                            temp.append(td.text)
                            print('Case id               :', temp[0])

                        #date of order
                        if td_counter==2:
                            temp=[]
                            temp.append(td.text)
                            print('Date of Order         :', temp[0])
                            
                            '''
                            date=datefinder.find_dates(temp_str)
                            for i in date:
                                date=i 
                            case.date=date
                            case.year = date.strftime("%Y")
                            '''
                        
                        #Description and pdf link
                        if td_counter==3:
                            print('Description           :', td.text)
                            a_tags = td.find_elements(By.TAG_NAME,"a")
                            for a_tag in a_tags:
                                print('Pdf link              :', a_tag.get_attribute('href'))

                        #skipping sections for td_counter=4
                        #Judges
                        if td_counter==5:
                            
                            #names=temp[0].split(',')
                            print("Order Passed By       :", td.text)
                #spacing b/w orders
                print()
            
            #going back to section/yr page
            driver.back()

    #going back to home for selecting the next bench
    driver.back()

#closing the chrome instance/window
driver.quit()

















