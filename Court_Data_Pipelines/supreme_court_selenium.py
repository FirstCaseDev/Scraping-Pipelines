from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
PATH = r"C:\\Users\\risha\\Downloads\\chromedriver.exe"
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

#driver = webdriver.Chrome(PATH,chrome_options=options) #Headless
driver = webdriver.Chrome(PATH)

# WebDriverWait wait = new WebDriverWait(webDriver, timeoutInSeconds);
# wait.until(ExpectedConditions.visibilityOfElementLocated(By.id<locator>));

#driver.implicitly_wait(3)

driver.get("https://main.sci.gov.in/judgments")
wait = WebDriverWait(driver,10)
time.sleep(5) #search = wait.until(EC.element_to_be_clickable((By.ID,'tabbed-nav')))
driver.find_element_by_xpath("//*[@id='tabbed-nav']/ul[2]/li[3]/a").click() #select tab


search = driver.find_element_by_xpath("//*[@id='cap']/font")
captha= search.text
search=driver.find_element_by_xpath("//*[@id='ansCaptcha']")
search.click()
search.send_keys(captha)
start_date="03-02-2021"
end_date="04-02-2021"
wait = WebDriverWait(driver,10)
search = wait.until(EC.element_to_be_clickable((By.ID,'JBJfrom_date')))
search = driver.find_element_by_xpath("//*[@id='JBJfrom_date']")

search.clear()
search.send_keys(start_date)

wait = WebDriverWait(driver,10)
search = wait.until(EC.element_to_be_clickable((By.ID,'JBJto_date')))
search = driver.find_element_by_xpath("//*[@id='JBJto_date']")
search.clear()
search.send_keys(end_date)
search = driver.find_element_by_xpath("//*[@id='v_getJBJ']") # clicked submit button after entering dates
search.click()
# Captcha filled and dates entered. Now we will have to collect data


WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.ID,"JBJ")))
table_id = driver.find_element_by_id("JBJ")
WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,"//*[@id='JBJ']/table")))
table = table_id.find_element_by_tag_name("table")
table_body = table.find_element_by_tag_name("tbody")
rows = table_body.find_elements(By.TAG_NAME, "tr")
counter = 0
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
            counter = counter + 1
            #print(a_tag.text)
            if count >0:
                break
            url = a_tag.get_attribute('href')
            count = count + 1        
        case_list.append(c.text)
        #print(counter2)
        #print (c.text)
        if counter2 == 20:
            sn = case_list[0]
            print (case_list)
            print(sn)
            print(url)
            case_list = []
            counter2 = 0
#print(case_list)
#print(counter/2)
#x = int(counter/2)
#case_list = ""
# for i in range(0, x):
#     if len(c.text) ==0:
#         break
#     else:
#case_list = case_list.append(c.text)

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
