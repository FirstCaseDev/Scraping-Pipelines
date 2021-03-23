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

#setting up the driver
PATH='C://Program Files (x86)//chromedriver.exe'
driver= webdriver.Chrome(PATH)

#Headless
#driver = webdriver.Chrome(PATH,chrome_options=options) 

#opening an instance @bombay HC
driver.get('https://bombayhighcourt.nic.in/')


#accessing services -> orders & judgement -> rept. judgement/orders
#services
driver.find_element_by_xpath('//*[@id="smoothmenu1"]/ul[4]/li/a').click()
time.sleep(1)

#orders_and_judgement
driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[2]/th/table/tbody/tr/td/div/ul[4]/li/ul/li[2]/a').click()
time.sleep(1)

#Rept_judgement/orders
driver.find_element_by_xpath('//*[@id="smoothmenu1"]/ul[4]/li/ul/li[2]/ul/li[3]/a').click()
time.sleep(1)


#accessing respective fields 

#field-1--Side
#then selecting desired side
side=driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td[2]/select').click()
time.sleep(1)

side_select=driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td[2]/select/option[1]').click()



#field-2--Act
#then selecting desired act
act=driver.find_element_by_xpath('/html/body/form/table[3]/tbody/tr/td[3]/select').click()
time.sleep(1)

act_select=driver.find_element_by_xpath('/html/body/form/table[3]/tbody/tr/td[3]/select/option[1]').click()



#field-3--date
#then filling desired dates
current_day=datetime.date.today()
week_control=current_day-datetime.timedelta(days=7)
from_date=week_control.strftime('%d-%m-%Y')

#curretnt date
to_date=datetime.date.today().strftime('%d-%m-%Y')

#entering from date into the box
search_from_date=driver.find_element_by_xpath('//*[@id="demo1"]')
driver.execute_script('document.getElementsByName("frmdate")[0].removeAttribute("onfocus")')
search_from_date.send_keys(from_date)
time.sleep(1)

#entering to date into the box
search_to_date=driver.find_element_by_xpath('//*[@id="demo2"]')
driver.execute_script('document.getElementsByName("todate")[0].removeAttribute("onfocus")')
search_to_date.send_keys(to_date)
time.sleep(1)



#field-4--Security code--Captcha
security_code=driver.find_element_by_xpath('/html/body/form/table[6]/tbody/tr/td[2]/img').get_attribute("alt")
enter_text=driver.find_element_by_xpath('/html/body/form/table[6]/tbody/tr/td[2]/input[2]')
enter_text.send_keys(security_code)
time.sleep(1)

#submit button
driver.find_element_by_xpath('/html/body/form/table[7]/tbody/tr/td[1]/input').click()
time.sleep(2)



#scrapping page's data
case=CaseDoc()
#loacting target table for scrapping

table=driver.find_element_by_xpath('/html/body/form/table[2]')
t_body=table.find_element_by_tag_name('tbody')

rows=t_body.find_elements(By.TAG_NAME,'tr')

#column_headings=['Coram','Party','Judgment date and Bench','Case no. and Upload date']

row_counter=0
total_rows=0

#accounting total no. of rows
for row in rows:
    total_rows+=1

#traversing through rows of the table
for row in rows:
    
    row_counter+=1

    #skipping extra (starting, in-between and ending) rows 
    if row_counter>=5 and row_counter%2!=0 and row_counter<total_rows-1: 
        
        td_counter=0
        total_td=0
        
        tds=row.find_elements(By.TAG_NAME,'td')

        #caculating no. of td(s)
        for z in tds:
            total_td+=1

        #traversing through data points
        for c in tds:
            td_counter+=1


            #printing field specific data
            #coram field                
            if td_counter==2:
                temp=[]
                temp.append(c.text)
                temp_str=temp[0]
                #print('Judge(s)        :',temp_str)


            #parties distinguished
            if td_counter==3:
                temp=[]
                temp.append(c.text)
                temp_str=temp[0]
                indice_1=temp_str.find(' Vs ')
                #print('Petitioner Name :',temp_str[:indice_1])
                case.petitioner=temp_str[:indice_1]
                #print('Respondent Name :', temp_str[indice_1+4:])
                case.respondent=temp_str[indice_1+4:]


            #judgement date and bench seperation
            if td_counter==4:
                temp=[]
                temp.append(c.text)
                temp_str=temp[0]
                
                #print('Judgement Date  :',temp_str[:10])
                date=datefinder.find_dates(temp_str[:10])
                for i in date:
                    date=i 
                case.date=date
                case.year = date.strftime("%Y")
                #print('Bench           :',temp_str[11:])
                case.bench=temp_str[11:]
                case.source='High Court of Bombay'

            #case no. and pdf seperation
            if td_counter==5:
                temp=[]
                temp.append(c.text)
                temp_str=temp[0]
                indice_1=temp_str.find('(')
                indice_2=temp_str.find(')')
                
                #print('Case Number     :', temp_str[:indice_1])
                case.case_id=temp_str[:indice_1]
                #print('Upload Date    :', temp_str[indice_2+2:])

                a_tags = c.find_elements(By.TAG_NAME,"a")
                for a_tag in a_tags:
                    #print('Pdf link        :',a_tag.get_attribute('href'))                        
                    pdf_link=a_tag.get_attribute('href')
                    case.url=pdf_link
                    judgement_txt=extract_txt(pdf_link, 'Bombay_High_Court_Extract.pdf')
                    case.judgement_text=judgement_txt

            #cross-checking-- if case already present then skip
            #              -- if not then process the extracted data
            
            if case_exists_by_case_id(case.case_id):
                continue

        #spacing between cases        
        #print()

        #processing all the extracted data
        case.process_text()
        case.print_case_attributes()
        store_case_document(case)


#closing window/instance
driver.quit()
















