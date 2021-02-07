from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located

PATH = "C:\\Users\\punee\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://main.sci.gov.in/judgments")
driver.find_element_by_xpath("//*[@id='tabbed-nav']/ul[2]/li[3]/a").click()  # select tab
search = driver.find_element_by_xpath("//*[@id='cap']/font")
captcha = search.text
search = driver.find_element_by_xpath("//*[@id='ansCaptcha']")
search.click()
search.send_keys(captcha)
start_date = "01-02-2021"
end_date = "05-02-2021"
search = driver.find_element_by_xpath("//*[@id='JBJfrom_date']")
search.clear()
search.send_keys(start_date)
search = driver.find_element_by_xpath("//*[@id='JBJto_date']")
search.clear()
search.send_keys(end_date)
search = driver.find_element_by_xpath("//*[@id='v_getJBJ']")
search.click()
WebDriverWait(driver,10).until(presence_of_all_elements_located((By.ID,"JBJ")))
table_id = driver.find_element_by_id("JBJ")
WebDriverWait(driver,10).until(presence_of_all_elements_located((By.XPATH,"//*[@id='JBJ']/table")))
table = table_id.find_element_by_tag_name("table")
table_body = table.find_element_by_tag_name("tbody")
rows = table_body.find_elements(By.TAG_NAME, "tr")
for row in rows:
    col = row.find_elements(By.TAG_NAME,"td")
    for c in col:
        a_tags = c.find_elements(By.TAG_NAME,"a")
        for a_tag in a_tags:
            print(a_tag.text)
            print(a_tag.get_attribute('href'))
        print (c.text)
    # print("......................................................")
driver.quit() #to close browser window