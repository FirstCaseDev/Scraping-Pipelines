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


#opening an instance @greentribunal.gov.in/judgementOrder/zonalbenchwise
driver.get('https://greentribunal.gov.in/judgementOrder/zonalbenchwise')
time.sleep(1)

#scrapping page's data
case=CaseDoc()

#loop for selecting different benches(5)
for bench in range(2,7):
    
    #selecting bench
    driver.find_element_by_xpath('//*[@id="search-party-name-form"]/div/div[1]/select').click()
    bench_name=driver.find_element_by_xpath('//*[@id="search-party-name-form"]/div/div[1]/select/option[{bench_index}]'.format(bench_index= bench)).text
    driver.find_element_by_xpath('//*[@id="search-party-name-form"]/div/div[1]/select/option[{bench_index}]'.format(bench_index= bench)).click()


    #setting start/end date- (past 1 week)
    current_day=datetime.date.today()
    week_control=current_day-datetime.timedelta(days=7)
    from_date=week_control.strftime('%d/%m/%Y')

    #curretnt date
    to_date=datetime.date.today().strftime('%d/%m/%Y')

    #filling the dates
    from_day_box = driver.find_element_by_xpath('//*[@id="fromdate"]')
    from_day_box.click()
    from_day_box.send_keys(from_date)

    to_day_box = driver.find_element_by_xpath('//*[@id="todate"]')
    to_day_box.click()
    to_day_box.send_keys(to_date)

    #selecting searching criteria
    search_box = driver.find_element_by_xpath('//*[@id="search-party-name-form"]/div/div[4]/select')
    search_box.click()
    driver.find_element_by_xpath('//*[@id="search-party-name-form"]/div/div[4]/select/option[2]').click()

    #solving captcha
    captcha_txt=driver.find_element_by_xpath('//*[@id="mainCaptcha"]').text
    #print(captcha_txt)
    captcha_box = driver.find_element_by_xpath('//*[@id="txtInput"]')
    captcha_box.click()
    captcha_box.send_keys(captcha_txt)

    #search button
    driver.find_element_by_xpath('//*[@id="search-party-name-form"]/div/div[6]/button').click()
    time.sleep(1)

    #calculating total page count for the selected bench
    #ul tag
    ul=driver.find_element_by_xpath('//*[@id="block-system-main"]/div/div/div[2]/div/ul')

    #li tags
    lis = ul.find_elements(By.TAG_NAME, 'li')
    pg_counter=0
    for li in lis:
        pg_counter+=1
    
    #excludind links-prev/next/last
    total_pg=pg_counter-3
    #print(total_pg)

    #for benches having one pg only
    if total_pg==0:
        total_pg=1
        
    #if no data is present    
    if total_pg==-1:
        driver.back()
        continue

    #counter to maintain next page accessing code    
    nxt_pg_counter=0

    #for scrapping all pages
    for page in range(total_pg):
        
        #loacting target table for scrapping
        table=driver.find_element_by_xpath('//*[@id="block-system-main"]/div/div/div[2]/table')
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

            td_counter=0
            #td tags
            #using xpath instead of find-td as element gets detached from the current page as driver comes back from pdf page
            #rows_new=driver.find_element_by_xpath('//*[@id="block-system-main"]/div/div/div[2]/table').find_elements(By.TAG_NAME,'tr')

            row_new=driver.find_element_by_xpath('//*[@id="block-system-main"]/div/div/div[2]/table/tbody/tr[{tr_index}]'.format(tr_index= row_counter))
            tds=row_new.find_elements(By.TAG_NAME, 'td')
            
            '''
            #caculating total no. of td(s) tags
            total_td=0
            for z in tds:
                total_td+=1
            '''

            for td in tds:
                td_counter+=1

                #bench name                
                if td_counter==2:
                    temp=[]
                    temp.append(td.text)
                    slice_1=temp[0].find('(')
                    b_name= temp[0][:slice_1]

                    #print('Bench name              :', b_name)
                    


                #diary number  
                if td_counter==3:
                    temp=[]
                    temp.append(td.text)
                    d_no=temp[0]

                    #print('Diary number            :', d_no)
                    

                
                #case number  
                if td_counter==4:
                    temp=[]
                    temp.append(td.text)
                    slice_1=temp[0].find('No.')
                    case_no=temp[0][slice_1+4:]

                    #print('Case number             :', case_no)
                    


                #petitioner & respondent
                if td_counter==5:
                    temp=[]
                    temp.append(td.text)
                    temp_str=temp[0]
                    slice_1=temp_str.find('VS')
                    pet=temp_str[0:slice_1]                                        
                    res=temp_str[slice_1+3:]

                    #print('Petitioner              :', pet)
                    #print('Respondent              :', res)
                    
                    


                #date of judgement
                if td_counter==6:
                    temp=[]
                    temp.append(td.text)
                    doj= temp[0]

                    #print('Date of Judgement       :', doj)
                                            
                    date=datefinder.find_dates(temp[0])
                    for i in date:
                        date=i 
                    

                #checking if status is disposed or not    
                if (td_counter==7) and (td.text=='PENDING'):
                    continue

                #pdf link(s)
                if (td_counter==7) and (td.text=='DISPOSED'):

                    print('Bench name              :', b_name)
                    #print('Diary number            :', d_no)
                    #print('Case number             :', case_no)
                    #print('Petitioner              :', pet)
                    #print('Respondent              :', res)
                    #print('Date of Judgement       :', doj)
                    #print('Case status             :', td.text)

                    #case.source = b_name
                    #case.case_id = d_no
                    #case.case_id = case_no
                    #case.petitioner = pet
                    #case.respondent = res
                    #case.date=date
                    #case.year = date.strftime("%Y")

                    
                    #entering another pg to get judgement pdf
                    a_tag=td.find_element_by_tag_name('a')
                    a_tag.click()
                    time.sleep(1)
                    
                    #accessing the listing history section
                    driver.find_element_by_xpath('//*[@id="headingThree"]/a').click()
                    time.sleep(1)

                    table=driver.find_element_by_xpath('//*[@id="collapseThree"]/div/div/table')
                    t_body=table.find_element_by_tag_name('tbody')
                    rows=t_body.find_elements(By.TAG_NAME,'tr')


                    #coram/judges
                    coram=driver.find_element_by_xpath('//*[@id="collapseThree"]/div/div/table/tbody/tr[1]/td[4]')
                    judges=coram.text
                    print('Judge(s)                :', judges)

                    case.bench=judges
                    

                    #selecting all the a tags of table
                    for row in rows:
                        a_tags = row.find_elements(By.TAG_NAME,"a")
                        
                        for a_tag in a_tags:
                            onclick= a_tag.get_attribute('onclick')
                            slice_1=onclick.find("'")
                            slice_2=onclick.find(")")
                            link_pretext='greentribunal.gov.in/gen_pdf_test.php?filepath='
                            
                            #combining the link_pretext to complete the link
                            pdf_link = link_pretext + onclick[slice_1+1:slice_2-1]
                            print('Pdf link(s)             :', pdf_link)
                            
                            #case.url=pdf_link
                            #judgement_txt=extract_txt(pdf_link, 'Court_Extract.pdf')
                            #case.judgement_text=judgement_txt
            
                    #going back to case list pg
                    driver.back()
                    #spacing b/w judgemnets
                    print()            

            #processing all the extracted data
            #case.process_text()
            #case.print_case_attributes()
            #store_case_document(case)
        
        #going to the next pg
        next_pg=driver.find_element_by_xpath('//*[@id="block-system-main"]/div/div/div[2]/div/ul/li[{pg_index}]/a'.format(pg_index=page+3))
        if next_pg.text != 'Next':
            nxt_pg_counter+=1
            next_pg.click()
            time.sleep(1)

    #going back to bench selection
    driver.execute_script('window.history.go({pg})'.format(pg = -(total_pg)))   


#closing chrome instance/window
driver.quit() 


