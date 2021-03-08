from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.alert import Alert 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import timedelta,date
from Common_Files.Case_pdf_handling import extract_txt
from Common_Files.Case_storage import store_case_document
from Common_Files.Case_handler import CaseDoc 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from datetime import date,timedelta
from PIL import Image
import pytesseract 
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
import requests

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

PATH = "C:\Program Files (x86)\chromedriver.exe"
# driver = webdriver.Chrome(PATH)
driver = webdriver.Chrome(PATH,chrome_options=options) #Headless


def Madras_court():
    driver1 = driver.get("https://services.ecourts.gov.in/ecourtindiaHC/cases/s_orderdate.php?state_cd=10&dist_cd=1&court_code=1&stateNm=Madras")
    time.sleep(2)

def Calcutta_court():
    driver.get('https://services.ecourts.gov.in/ecourtindiaHC/cases/s_orderdate.php?state_cd=16&dist_cd=1&court_code=1&stateNm=Calcutta')
    time.sleep(2)

def captcha_reader():
    time.sleep(2)
    captcha_element = driver.find_element(By.XPATH,'//*[@id="captcha_image"]')
    driver.save_screenshot('screenshot.png')
    im = Image.open("screenshot.png")
    # crop = im.crop((440,340,540,370))
    crop = im.crop((200,250,340,300))
    crop.show()
    captcha_text = pytesseract.image_to_string(crop).strip()
    print('Captcha '+ captcha_text)
    digits_in_captcha =''.join(c for c in captcha_text if c.isdigit())
    print('Captcha Text: '+ digits_in_captcha)
    
    print(len(digits_in_captcha))
    search = driver.find_element_by_xpath('//*[@id="captcha"]')
    search.send_keys(captcha_text)

def date_input():
    today = date.today()
    enddate = today - timedelta(days=7)
    F = enddate.strftime("%d-%m-%Y")
    E = today.strftime("%d-%m-%Y")
    from_date = driver.find_element_by_xpath('//*[@id="from_date"]')
    from_date.send_keys(F)
    end_date = driver.find_element_by_xpath('//*[@id="to_date"]')
    end_date.send_keys(E)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="caseNoDet"]/div[2]/span[3]/img').click()
    time.sleep(2)

Calcutta_court()

captcha_reader()          

date_input()
driver.find_element_by_xpath('//*[@id="caseNoDet"]/div[4]/span[3]/input[1]').click() ## submit button
alert = Alert(driver)
try:
    if alert.is_displayed():
        alert = Alert(driver)
        print(alert)
        alert.accept()
        time.sleep(5)
        captcha_reader()
        driver.find_element_by_xpath('//*[@id="caseNoDet"]/div[4]/span[3]/input[1]').click() ## submit button
except:
    while  driver.find_element(By.XPATH,'//*[@id="txtmsg"]').is_displayed()== True:
        driver.find_element(By.XPATH,'//*[@id="caseNoDet"]/div[4]/span[3]/input[2]').click() ## click on reset button
        driver.find_element(By.XPATH,'//*[@id="caseNoDet"]/div[1]/span[3]/img').click()  ## click on calendar icon
        print("Reset")
        time.sleep(2)
        try :
            captcha_reader()
            time.sleep(2)
            date_input()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="caseNoDet"]/div[4]/span[3]/input[1]').click() ### click on submit button
            time.sleep(10)
        except:
            continue

    if (driver.find_element(By.XPATH,'//*[@id="showList1"]/tr[1]/td[1]').is_displayed()) == True: #this is the first element on result table if it is shown then proceeds.
        table = driver.find_element_by_xpath('//*[@id="showList1"]')
        rows = table.find_elements(By.TAG_NAME,"tr")

        for row in rows:
            col = row.find_elements(By.TAG_NAME,"td")
            Sno = col[0].text
            for c in col:
                a_tags = c.find_elements(By.TAG_NAME,"a")
                for a_tag in a_tags:
                        case_url = a_tag.get_attribute("href")
                        print("1")
                        print(c.text)
                        print("2")
                        print(col[2].text)
                        print("3")
                        print(case_url)
        links = driver.find_elements_by_link_text('Judgement')  
        for link in links:
            case_url = link.get_attribute("href")
            print(case_url)              
            
driver.quit()