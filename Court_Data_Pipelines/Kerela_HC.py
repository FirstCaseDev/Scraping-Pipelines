from selenium import webdriver
import time
import datetime
import datefinder
import pymongo
import pytesseract
import requests
from cv2 import cv2
from PIL import Image
from io import BytesIO
from Common_Files.Case_pdf_handling import extract_txt
from Common_Files.Case_storage import store_case_document, case_exists_by_case_id
from Common_Files.Case_handler import CaseDoc 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

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

#opening an instance @KERELA HC --> ORDER DATE
driver.get('https://services.ecourts.gov.in/ecourtindiaHC/cases/s_orderdate.php?state_cd=4&dist_cd=1&court_code=1&stateNm=Kerala')
time.sleep(1)



#filling captcha
captcha = driver.find_element_by_xpath('//*[@id="captcha_image"]')
'''
#method 1
#taking screenshot of pg -->cropping the captcha img-->converting img to text using tesseract
driver.save_screenshot('screenshot.png')
cap_loc=captcha.location

image = cv.imread(cv.samples.findFile('screenshot.png', True))
out = cv.CreateImage((150,60), image.depth, 3)
cv.SetImageROI(image, (cap_loc['x'],cap_loc['y'],150,60))
cv.Resize(image, out)
cv.SaveImage('out.jpg', out)

cap_img=Image.open(captcha.get_attribute('out.jpg'))
cap_text=pytesseract.image_to_string(cap_img)
'''

'''
#method 2
#using urllib
import urllib
# get the image source
cap_src = captcha.get_attribute('src')
# download the image
urllib.urlretrieve(cap_src, 'captcha.png')
cap_img = Image.open('captcha.png')
cap_text = pytesseract.image_to_string(cap_img)


#using requests and bytesio from io
r=requests.get(captcha.get_attribute('src'))
img=Image.open(BytesIO(r.content))
img.save('captcha.jpeg')
'''

#method 3
# taking screenshot(as captcha changes each time it is accessed) --> cropping captcha --> str to text convertion via tesseract
driver.save_screenshot('screenshot.png')
img_ss = cv2.imread('screenshot.png')
#print(img_ss.shape)
#cv2.imshow('1', img_ss)
#format--> (y axis, x axis, rbg code)

#cropping
#matrix format--> (y,x)
img_cropped= img_ss[265:300,350:430]
#cv2.imshow('3', img_cropped)
#cv2.waitKey(0)
 
cap_text = pytesseract.image_to_string(img_cropped)
captcha = cap_text[0:6]
#print(captcha)

captcha_box = driver.find_element_by_xpath('//*[@id="captcha"]')
captcha_box.send_keys(captcha)


#setting start/end date- (past 1 or 2 days -- due to huge amount of orders)
current_day=datetime.date.today()
week_control=current_day-datetime.timedelta(days=2)

from_date=week_control.strftime('%d-%m-%Y')
#format 15-04-2021
#print(from_date)

#curretnt date
to_date=datetime.date.today().strftime('%d-%m-%Y')
#print(to_date)


#filling up from/to dates
from_date_box = driver.find_element_by_xpath('//*[@id="from_date"]')
from_date_box.click()
from_date_box.send_keys(from_date)

to_date_box = driver.find_element_by_xpath('//*[@id="to_date"]')
to_date_box.click()
to_date_box.send_keys(to_date)



#go button
driver.find_element_by_xpath('//*[@id="caseNoDet"]/div[4]/span[3]/input[1]').click()
time.sleep(1)



#scrapping page's data           
case=CaseDoc()

#loacting target table for scrapping
table=driver.find_element_by_xpath('//*[@id="showList3"]')
t_body=table.find_element_by_tag_name('tbody')

rows=t_body.find_elements(By.TAG_NAME,'tr')

row_counter=0

for row in rows:

    row_counter+=1
    print(row_counter)

    td_counter=0
                                        
    tds=row.find_elements(By.TAG_NAME,'td')
    
    
    #bench name
    print('Bench                 : Kerela HC')

    for td in tds:
        td_counter+=1

        #case-id --> (Case Type/Case Number/Case Year)<-- format
        if td_counter==2:
            temp=[]
            temp.append(td.text)
            print('Case id              :', temp[0])

        #order date (dd-mm-yyyy)
        if td_counter==3:
            temp=[]
            temp.append(td.text)
            print('Date of Order         :', temp[0])
                                        
            date=datefinder.find_dates(temp[0])
            for i in date:
                date=i 
            case.date=date
            case.year = date.strftime("%Y")

        #pdf link and order type
        if td_counter==4:
            temp=[]
            temp.append(td.text)
            print('Order type:          :', temp[0])

            a_tags=td.find_elements(By.TAG_NAME, 'a')
            for a_tag in a_tags:
                print('pdf link             :', a_tag.get_attribute('href'))



#closing the chrome instance
driver.close()



