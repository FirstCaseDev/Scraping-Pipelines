from selenium import webdriver
import time
import pymongo
import datefinder
#from Article_extractor import article_get_acts_list, article_get_cases_list, article_get_length
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.chrome.options import Options


#accessing the article storage
client = pymongo.MongoClient('mongodb://db_user:firstCaseDevTeam@107.20.44.181:27017,3.229.151.98:27017,54.175.129.116:27017/?authSource=admin&replicaSet=aName&readPreference=primaryPreferred&ssl=false')
db = client["article_data"]
col = db["articles"]


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

#opening an instance @Manupatrafast.com --> articles
driver.get('https://www.manupatrafast.com/articles/articleSearch.aspx')
time.sleep(1)

#getting total number of records
total_records=int(driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_lblTotalRecords"]').text)
#print(total_records)

#calculating looping constraint
#div by 10 as each pg contains 10 articles

if total_records//10 < total_records/10 :
    n_pages = (total_records//10) + 1
else:
    n_pages = total_records//10

#print(n_pages)

#1  //*[@id="ctl00_ContentPlaceHolder1_grdArticles"]/tbody/tr[42]/td/table/tbody/tr/td[1]/span
#1  //*[@id="ctl00_ContentPlaceHolder1_grdArticles"]/tbody/tr[42]/td/table/tbody/tr/td[1]/a   (while on 2nd pg)
#2  //*[@id="ctl00_ContentPlaceHolder1_grdArticles"]/tbody/tr[42]/td/table/tbody/tr/td[2]/a
#3  //*[@id="ctl00_ContentPlaceHolder1_grdArticles"]/tbody/tr[42]/td/table/tbody/tr/td[3]/a
#4  //*[@id="ctl00_ContentPlaceHolder1_grdArticles"]/tbody/tr[42]/td/table/tbody/tr/td[4]/a
#.  //*[@id="ctl00_ContentPlaceHolder1_grdArticles"]/tbody/tr[42]/td/table/tbody/tr/td[11]/a
#11 //*[@id="ctl00_ContentPlaceHolder1_grdArticles"]/tbody/tr[42]/td/table/tbody/tr/td[2]/span
#12 //*[@id="ctl00_ContentPlaceHolder1_grdArticles"]/tbody/tr[42]/td/table/tbody/tr/td[3]/a
#.  //*[@id="ctl00_ContentPlaceHolder1_grdArticles"]/tbody/tr[42]/td/table/tbody/tr/td[12]/a
#22 //*[@id="ctl00_ContentPlaceHolder1_grdArticles"]/tbody/tr[42]/td/table/tbody/tr/td[3]/a


#page counter
pg_counter=0

#loop for iterating pages
for x in range(1,n_pages):

    pg_counter+=1

    #scrapping page's data
    #loacting target table for scrapping
    table=driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_grdArticles"]')
    t_body=table.find_element_by_tag_name('tbody')

    rows=t_body.find_elements(By.TAG_NAME,'tr')
    row_counter=0
    
    '''
    #accounting total no. of rows
    total_rows=0
    for row in rows:
        total_rows+=1
    print(total_rows) #42
    '''

    #for row_counter condition
    k=0

    #traversing through tr(s)
    for row in rows:
        row_counter+=1

        #since headings are in tr(s) 3,7,11,15,.....,39
        if (row_counter==3) or (row_counter==3+4*(k) and row_counter<40):
            k+=1
            
            #Accessing article link/Name
            #using xpath instead of find-td as element gets detached from the current page as driver comes back from article page
            td=driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_grdArticles"]/tbody/tr[{0}]/td'.format(row_counter))
                
            a_tag = td.find_element(By.TAG_NAME,"a")
            article_name=a_tag.text
            print('Article Name             :', article_name)
            
            #accessing individual article page
            a_tag.click()
            time.sleep(1)

            pdf=driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_grdSearch_ctl02_ifrm"]')
            pdf_url=pdf.get_attribute('src')
            print('pdf link                 :', pdf_url)

            #going back to main page
            driver.back()
            time.sleep(1)
        
        #condition to get Author/Subject/Date/Category(asdc) as they occur in tr(s) 5,9,14,19,...,41
        if (row_counter==5) or (row_counter==(5+4*(k-1)) and row_counter < 42 and row_counter>3):
            #print(k)

            #using xpath instead of find-td as element gets detached from the current page as driver comes back from article page
            asdc=driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_grdArticles"]/tbody/tr[{0}]/td/h6'.format(row_counter))
            
            #print(asdc.text)

            temp_str=asdc.text
            a_slice=temp_str[temp_str.find('Author:')+8 : temp_str.find('|')]
            temp_str=temp_str[temp_str.find('|')+1 :]

            s_slice=temp_str[temp_str.find('Subject:')+9 : temp_str.find('|')]
            temp_str=temp_str[temp_str.find('|')+1 :]

            d_slice=temp_str[temp_str.find('Date:')+6 : temp_str.find('|')]
            temp_str=temp_str[temp_str.find('|')+1 :]

            c_slice=temp_str[temp_str.find('(')+1 : temp_str.find(')')]
            
            print('Author name              :', a_slice)
            print('Subject                  :', s_slice)
            print('Date                     :', d_slice)
            print('Category                 :', c_slice)

            #spacing b/w articles
            print()







    '''
    #condition for pg_counter
    if:
    
    else:
    '''





#closing chrome istance/window
driver.quit()












