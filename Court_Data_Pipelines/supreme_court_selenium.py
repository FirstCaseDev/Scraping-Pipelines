'''
>> Import Necesaary Modules
>> Mention ChromeDriver Path in PATH variable
'''

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
PATH = r"C:\\Users\\risha\\Downloads\\chromedriver.exe"
from selenium.webdriver.chrome.options import Options
from Common_Files.Case_pdf_handling import extract_txt
from Common_Files.Case_handler import CaseDoc
import datefinder
from Common_Files.Case_storage import store_case_document
import datetime as DT

'''
Extraction of today's date
'''
today = DT.date.today() #Today's date
today_str = today.strftime("%Y-%m-%d")
update_today = DT.datetime.strptime(today_str, '%Y-%m-%d').strftime('%d-%m-%Y')
#update_today_str = today.strftime("%d-%m-%Y")

week_ago = today - DT.timedelta(days=7) # number of days we want to go back
week_ago_str = week_ago.strftime("%Y-%m-%d")
update_week_ago = DT.datetime.strptime(week_ago_str, '%Y-%m-%d').strftime('%d-%m-%Y')
#update_week_ago_str = today.strftime("%d-%m-%Y")
#print(update_today)
#print(update_week_ago)

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

#driver = webdriver.Chrome(PATH,chrome_options=options) #For running Chromedriver Headless
driver = webdriver.Chrome(PATH)

# WebDriverWait wait = new WebDriverWait(webDriver, timeoutInSeconds);
# wait.until(ExpectedConditions.visibilityOfElementLocated(By.id<locator>));
#driver.implicitly_wait(3)

driver.get("https://main.sci.gov.in/judgments") 
wait = WebDriverWait(driver,10)
time.sleep(5) #search = wait.until(EC.element_to_be_clickable((By.ID,'tabbed-nav')))
driver.find_element_by_xpath("//*[@id='tabbed-nav']/ul[2]/li[3]/a").click() #select tab

search = driver.find_element_by_xpath("//*[@id='cap']/font") # Finding Captcha element
captcha= search.text # Captcha text extracted
search=driver.find_element_by_xpath("//*[@id='ansCaptcha']") # Finding Captcha box element
search.click() #Captcha box clicked
search.send_keys(captcha) # Captcha entered
start_date=update_week_ago
end_date=update_today

# start_date="01-01-2021"
# end_date="15-01-2021"
wait = WebDriverWait(driver,10) 

'''
Start date entered
'''
search = wait.until(EC.element_to_be_clickable((By.ID,'JBJfrom_date')))
search = driver.find_element_by_xpath("//*[@id='JBJfrom_date']")
search.clear()
search.send_keys(start_date)
wait = WebDriverWait(driver,10)

'''
End date entered
'''
search = wait.until(EC.element_to_be_clickable((By.ID,'JBJto_date')))
search = driver.find_element_by_xpath("//*[@id='JBJto_date']")
search.clear()
search.send_keys(end_date)

search = driver.find_element_by_xpath("//*[@id='v_getJBJ']") # clicked submit button after entering dates
search.click() # Captcha filled and dates entered. Now we will have to collect data

'''
>> Case data is stored in cells of table with id "JBJ"
>> Table ELement(id 'JBJ') is stored in table
>> Table Body(id - "tbody") is stored in variable table_body
>> Table rows(id - "tr") is stored in rows
>> Order of HTML tags is table > tbody > tr
'''

WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.ID,"JBJ")))
table_id = driver.find_element_by_id("JBJ")
WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,"//*[@id='JBJ']/table")))
table = table_id.find_element_by_tag_name("table")
table_body = table.find_element_by_tag_name("tbody")
rows = table_body.find_elements(By.TAG_NAME, "tr")

'''
>> Now we are extracting Columns from rows
>> Columns(id - "td") is stored in col variable
>> Order of HTML tags is table > tbody > tr > td
>> col is the list of all entries in the table
>> A for loop has been initiated to extract text from col(column list) using c.text
>> The text from the column(c.text) is then appended to the list case_list
>> It is observed that after every 20 column element new case starts
>> This means that elements from 1-20(Serial No. - '0-19' in col list) belongs to Case 1, From 21-40(Serial No. - '20-39' in col list) belongs to Case 2 and so on
>> For extracting url of Judgment text pdf another for loop is initiated to extract url using "href attribute"
>> case.process_text() extracts petitioner_counsel and respondent_counsel also so to overshadow that we will have to reassign them to new values which is already stored in case_list
'''

case_list = []
counter2 = 0
url = ""

for row in rows:
    col = row.find_elements(By.TAG_NAME,"td")
    for c in col:
        counter2 = counter2 +1
        a_tags = c.find_elements(By.TAG_NAME,"a")
        
        count = 0
        for a_tag in a_tags:
            #print(a_tag.text)
            if count >0:
                break
            url = a_tag.get_attribute('href')
            count = count + 1  

        case_list.append(c.text)
        if counter2 == 20:
            case = CaseDoc()
            sn = case_list[0]
            
            case.title = case_list[8] + " vs " + case_list[10]
            case.case_id = case_list[5]
            case.url = url
            dates = datefinder.find_dates(case_list[6])
            for i in dates:
                date = i
            case.date = date
            case.judgement_year = date.strftime("%Y")
            case.source = "Supreme Court of India"
            case.doc_author = case_list[18]
            case.petitioner = case_list[8]
            case.respondent = case_list[10]
            case.bench = case_list[16].split(",")
            case.judgement_text = extract_txt(url, 'supreme_court_judgement.pdf')
            case.process_text()

            case.petitioner_counsel = case_list[12].split(",")
            case.respondent_counsel = case_list[14].split(",")

            # store_case_document(case)

            #case.print_case_attributes()
            #print(case.title)
            #print(case.doc_author)
            #print (case_list)
            # print(sn)
            # print(url)
            #print(case.judgement_text)
            case_list = []
            counter2 = 0


driver.quit() #to close browser window


# import os
# os.system('pdf2txt.py -o pdf2html.html -t html xyz.pdf')
# os.system('pdf2txt.py -o pdf2text.txt xyz.pdf')

# with open('new-output.html', encoding="utf8") as file:
#     data_html = file.read()
#     print(data_html)

# with open('pdf2text.txt', encoding="utf8") as file:
#     data_txt = file.read()
#     print(data_txt)


print ("GG no Re")

        # self.title = ""                     #self defined   done
        # self.case_id = ""                    #self defined   done
        # self.url = ""                       #self defined   done
        # self.source = ""                    #self defined     done
        # self.date = datetime.datetime.now() #self defined   done
        # self.doc_author = ""                #self defined     done
        # self.petitioner = ""                #self defined     done
        # self.respondent = ""                #self defined     done
        # self.bench = []                     #self defined     done
        # self.petitioner_counsel = []        #function      done
        # self.respondent_counsel = []        #function      done
        # self.cases_cited = []               #function --- from case.process_text
        # self.cases_citing = []              #self defined --- not now
        # self.judgement = ""                 #function done   from case.process_text
        # self.judgement_text = ""            #self defined     done
        # self.provisions_referred = []       #function to be modified for datatype    from case.process_text
        # self.query_terms = []               #self defined  ---- not now
