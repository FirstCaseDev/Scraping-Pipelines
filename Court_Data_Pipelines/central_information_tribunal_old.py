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


#opening an instance @dsscic.nic.in/cause-list-report-web/view-decision-old-all/1-->old before 10th September 2016
driver.get('https://dsscic.nic.in/cause-list-report-web/view-decision-old-all/1')
time.sleep(1)

'''
#setting start/end date- (past week)
current_day=datetime.date.today()
week_control=current_day-datetime.timedelta(days=1)
from_date=week_control.strftime('%d/%m/%Y')

#curretnt date
to_date=datetime.date.today().strftime('%d/%m/%Y')

#filling the dates
from_day_box = driver.find_element_by_xpath('//*[@id="datetimepicker1"]/input')
#from_day_box.click()
from_day_box.send_keys(from_date)

to_day_box = driver.find_element_by_xpath('//*[@id="datetimepicker2"]/input')
#to_day_box.click()
to_day_box.send_keys(to_date)
'''


#scrapping page's data
case=CaseDoc()


#function to scrape page's data
def central_info_tribunal_old_scrapper():
    
    #loacting target table for scrapping
    t_body=driver.find_element_by_xpath('//*[@id="wrapperContent"]/div/div/div/section/div/div/div/table/tbody[2]')
                                        
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

        #skipping empty row
        if row_counter>1:

            #accessing td tags(columns) of each table row
            for td in tds:
                td_counter+=1
                
                #file no. 
                if td_counter==2:
                    temp=[]
                    temp.append(td.text)
                    print('File id                     :', temp[0])

                    #case.case_id = temp[0]
                    #case.source = 'Central Information Tribunal'

                #petitioner(applicant)
                if td_counter==3:
                    temp=[]
                    temp.append(td.text)                             
                   
                    print('Petitioner                  :', temp[0])

                    #case.petitioner = l[0][:-1]
                   

                #IC name--> td_counter==4:


                #date of order
                if td_counter==6:
                    temp=[]
                    temp.append(td.text)
                    print('Date of Order               :', temp[0])
                                        
                    date=datefinder.find_dates(temp[0])
                    for i in date:
                        date=i 

                    #case.date=date
                    #case.year = date.strftime("%Y")
                    


                '''                 ***pdf link isn't present***            '''
                if td_counter==8:
                    a_tags = td.find_elements(By.TAG_NAME,"a")
                    for a_tag in a_tags:
                        print('Pdf link                    :', a_tag.get_attribute('href'))
                        #pdf_link=a_tag.get_attribute('href')
                        #case.url=pdf_link
                        #judgement_txt=extract_txt(pdf_link, 'Court_Extract.pdf')
                        #case.judgement_text=judgement_txt

        
                        
        #spacing b/w judgemnets
        print()

        #processing all the extracted data
        #case.process_text()
        #case.print_case_attributes()
        #store_case_document(case)

#loop for decision types (main, interim, adjunct) 
for z in range(3):

    #accessing the decision types
    driver.find_element_by_xpath('//*[@id="decisiontypeid"]').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="decisiontypeid"]/option[{decision_index}]'.format(decision_index=z+2)).click()

    #go button
    driver.find_element_by_xpath('//*[@id="submit"]').click()
    time.sleep(1)

    #counting number of total pages
    pg_text=driver.find_element_by_xpath('//*[@id="wrapperContent"]/div/div/div/section/div/div/nav/div[1]').text
    index_1=pg_text.find('of')              
    index_2=pg_text.find('Pages')
    pg=pg_text[index_1+2:index_2]
    pg_no=''
    for num in pg:
        if num.isnumeric():
            pg_no+=num

    total_pg=int(pg_no)
    print(total_pg)

    #calling scrapper for desired number of pages
    for x in range(total_pg):
        
        #calling scarpper
        central_info_tribunal_old_scrapper()

        try:
            #accessing next button via index of last li tag
            ul=driver.find_element_by_xpath('//*[@id="wrapperContent"]/div/div/div/section/div/div/nav/div[2]/ul')
            lis=ul.find_elements(By.TAG_NAME, 'li')
            li_counter=0
            for li in lis:
                li_counter+=1

            #next button    
            driver.find_element_by_xpath('//*[@id="wrapperContent"]/div/div/div/section/div/div/nav/div[2]/ul/li[{li_index}]/a'.format(li_index=li_counter)).click()
            time.sleep(1)   

        except:
            print("Scraping stopped at page {} of {}".format(x+1,total_pg))


#closing chrome instance/window
driver.close()