from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\\Users\\Dell\\Desktop\\Firstcase ka bakheda\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://main.sci.gov.in/judgments")
driver.find_element_by_xpath("//*[@id='tabbed-nav']/ul[2]/li[3]/a").click()  # select tab
search = driver.find_element_by_xpath("//*[@id='cap']/font")
captcha = search.text
search = driver.find_element_by_xpath("//*[@id='ansCaptcha']")
search.click()
search.send_keys(captcha)
start_date = "01-12-2020"
end_date = "25-01-2021"
search = driver.find_element_by_xpath("//*[@id='JBJfrom_date']")
search.clear()
search.send_keys(start_date)
search = driver.find_element_by_xpath("//*[@id='JBJto_date']")
search.clear()
search.send_keys(end_date)
search = driver.find_element_by_xpath("//*[@id='v_getJBJ']")
search.click()

# driver.quit() to close browser window


# search = WebDriverWait(driver, 10).until(
#        EC.presence_of_element_located((By.ID,"cap"))
#    )
# captcha = search.getText()
# print(captcha)


# search = driver.find_elements_by_id('cap')
# print(search.text)
# search = driver.find_elements_by_id('captcha_image_audio_div')
# search.send_keys("5268")
# search = driver.find_element_by_id('v_getJBJ')
# search.send_keys(Keys.RETURN)

print("GG no Re")
