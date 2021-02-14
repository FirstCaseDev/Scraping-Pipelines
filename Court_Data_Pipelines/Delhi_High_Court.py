"""    Documentation For Delhi High Court Scraper

Functions Used
1. page_reader() : Used for navigating  to the elements on the Court orders page and storing the different data to their respective values on server and extracting 
    text from the pdf and storing it to server.

2. judgementDate():Used for navigating to the judgement date page where date is to be entered.

3. Calendar(D,M,Y,D2,M2,Y2):It takes date as input in DD MM YYYY format in which first from date is to be entered and then end date is to be entered for which it generates strings in format "DD/MM/YYYY" to be entered in 
   date section in judgement date page. ## changes to be made as Calendar is updated from old one

Working of Code :

From date is to be entered first and then end date is to be entered in then calendar funtion is called where it return a list of strings in date format then in try loop it enters the date string in date section and 
then page_reader Function is called if an error comes for no judgements on that date then except loop is called with NoSuchElementException.
After all the data is stored on server from that page then a try loop is called in which a while loop is called for checking link text for "Next" if exist then it goes to next page if not then except loop is continued.

        

"""
from datetime import date,timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Common_Files.Case_pdf_handling import extract_txt
from Common_Files.Case_handler import CaseDoc
from Common_Files.Case_storage import store_case_document
from selenium.webdriver.chrome.options import Options
import datefinder
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH,chrome_options=options) #Headless

# driver = webdriver.Chrome(PATH)



def page_reader():################# for Reading Contents of page when date is entered ###################
    
    case = CaseDoc()

    link = driver.find_element_by_xpath("/html/body/table[2]")
    table = link.find_element_by_xpath("/html/body/table[2]/tbody")
    rows = table.find_elements(By.TAG_NAME, "tr")
    rows.pop()
    
    for row in rows:
        col = row.find_elements(By.TAG_NAME,"td")
        Sno = col[0].text
        case_number = col[1].text
        case_title = col[3].text.replace("\n"," ").replace("\r"," ")
        case_petitioner = case_title.split("Vs")[0]
        case_respondent = case_title.split("Vs")[1]
        case.case_id = case_number
        dates = datefinder.find_dates(u)
        for i in dates:
            date = i

        for c in col:
        #     # print(c.text)
        #     # print(case_name) 
            a_tags = c.find_elements(By.TAG_NAME,"a")
            
            for a_tag in a_tags:
        #         # print(a_tag.text)
        #         # print(a_tag.get_attribute('href'))
                case_url = a_tag.get_attribute("href")
                
                judgement_text = extract_txt(case_url, "Delhi_High_Court_Extract.pdf")
        
        case.date = date
        case.source = "Delhi High Court"
        case.url = case_url
        case.petitioner = case_petitioner
        case.judgement_text = judgement_text
        case.title = case_title
        case.respondent = case_respondent
        case.process_text()
        # case.print_case_attributes()
        store_case_document(case) 
        
        


###############  navigate to JudgementDate Page ####################################        

             
             

def judgementDate():
    driver.get("http://164.100.69.66/jsearch/")
    # print(driver.title)
    link = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[@class='style13'][3]/b/input[@class='btn']")
    link.click()



###############################################################
            
def Calendar():
    dates = []
    today = date.today()
    todays_date = today.strftime("%d/%m/%Y")
    week_past = today - timedelta(days=7)
    week_past_date = week_past.strftime("%d/%m/%Y")
    
    diff = today - week_past       

    for i in range(diff.days + 1):
        day = today - timedelta(days=i)
        date_str = day.strftime("%d/%m/%Y")
        dates.append(date_str)
    return dates

############################################################################################

w=Calendar()


for i in range(len(w)):
    u = w[i]    
    judgementDate()
    
    try:
        driver.switch_to.frame("dynfr")
        input_box = driver.find_element_by_xpath("//*[@id='juddt']")
        driver.execute_script('document.getElementsByName("juddt")[0].removeAttribute("readonly")')
        input_box.clear()
        input_box.send_keys(u) 
        submit_btn = driver.find_element_by_name("Submit")
        submit_btn.click()
        driver.switch_to.default_content()
        
        frame = driver.find_element_by_name("dynfr")
        driver.switch_to.frame(frame)
        
        page_reader()
        
        try:
            while (driver.find_element_by_link_text("Next").click() == None):
                page_reader()

        except: 
            continue
    except NoSuchElementException:
        continue
        

driver.quit()
   # self.title = ""                     #self defined                done
        # self.case_id = ""                    #self defined          done
        # self.url = ""                       #self defined           done
        # self.source = ""                    #self defined           done
        # self.date = datetime.datetime.now() #self defined           done  
        # self.doc_author = ""                #self defined       from case.process_text    
        # self.petitioner = ""                #self defined         done
        # self.respondent = ""                #self defined         done
        # self.bench = []                     #self defined           
        # self.petitioner_counsel = []        #function            from case.process_text
        # self.respondent_counsel = []        #function      
        # self.cases_cited = []               #function --- from case.process_text
        # self.cases_citing = []              #self defined --- not now
        # self.judgement = ""                 #function done   from case.process_text
        # self.judgement_text = ""            #self defined     done
        # self.provisions_referred = []       #function to be modified for datatype    from case.process_text
        # self.query_terms = []               #self defined  ---- not now











