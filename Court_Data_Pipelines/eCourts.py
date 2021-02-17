from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import timedelta,date
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from PIL import Image
import pytesseract 
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
import requests

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# driver = webdriver.Chrome(PATH,chrome_options=options) #Headless


def Madras_court():
    driver1 = driver.get("https://services.ecourts.gov.in/ecourtindiaHC/cases/s_orderdate.php?state_cd=10&dist_cd=1&court_code=1&stateNm=Madras")
    time.sleep(10)

def Calcutta_court():
    driver.get('https://services.ecourts.gov.in/ecourtindiaHC/cases/s_orderdate.php?state_cd=16&dist_cd=1&court_code=1&stateNm=Calcutta')
    time.sleep(10)

def captcha_reader():
    err = False
    b=''
    while (err == False):
        try:
            captcha_element = driver.find_element(By.XPATH,'//*[@id="captcha_image"]')
            driver.save_screenshot('screenshot.png')
            im = Image.open("screenshot.png")
            crop = im.crop((350,270,440,300))
            captcha_text = pytesseract.image_to_string(crop)
            print('Captcha Text: '+ captcha_text)
            a = int(captcha_text)
            b = str(a)
            print('b: '+ b)
            print("Completed")
            err = True
        except:
            driver.find_element_by_xpath('//*[@id="captcha_container_2"]/div[1]/div/span[3]/a/img').click()
            err = False
            print('Reloading')
            time.sleep(5)
    return a

def captcha_writer(x):
    final_text = ''
    if (x<10000):          #if x is 4 or less digit number, add required zero(s) before x 
        iter_count = 0
        zero = '0'
        temp = x
        while temp>1:       #say limiting error is 1
            temp = temp//10
            iter_count = iter_count+1
            # print('===================================')
            # print('temp = ', temp)
            # print('iter_count = ', iter_count)
            # print('===================================')
        no_of_initial_zeroes = 5-iter_count
        for i in range(no_of_initial_zeroes):
            final_text = final_text + zero
        # print('initial zeroes: ' + final_text)
        final_text = final_text + str(x)
    
    else:
        final_text = str(x)

    # print('final captcha: ' + final_text)
    search = driver.find_element_by_xpath('//*[@id="captcha"]')
    search.send_keys(x)


def date_input():
    F = "01-01-2021"
    E = "14-01-2021"
    from_date = driver.find_element_by_xpath('//*[@id="from_date"]')
    from_date.send_keys(F)
    end_date = driver.find_element_by_xpath('//*[@id="to_date"]')
    end_date.send_keys(E)

Calcutta_court()

captcha = captcha_reader()          #captcha is integer data
captcha_writer(captcha)             #this convert captcha to string and sends to input box
date_input()
driver.find_element_by_xpath('//*[@id="caseNoDet"]/div[4]/span[3]/input[1]').click()
time.sleep(20)
table = driver.find_element_by_xpath('//*[@id="showList1"]')
rows = table.find_elements(By.TAG_NAME,"tr")

for row in rows:
    col = row.find_elements(By.TAG_NAME,"td")
    Sno = col[0].text
    for c in col:
        a_tags = c.find_elements(By.TAG_NAME,"a")
        for a_tag in a_tags:
            print(c.find_element_by_link_text("judgement"))
            case_url = a_tag.get_attribute("href")
            print(c.text)
            print(col.text)

# driver.quit()