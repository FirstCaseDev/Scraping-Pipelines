from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located

PATH = "C:\\Users\\punee\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://blog.ipleaders.in/blog/")
WebDriverWait(driver,30).until(presence_of_all_elements_located((By.CLASS_NAME,"popautoscroll")))
close_overlay = driver.find_elements_by_xpath("//*[@id='shwPopsCls']")
close_overlay[0].click()
WebDriverWait(driver,10).until(presence_of_all_elements_located((By.ID,"td_block_inner")))
blog_id = driver.find_elements_by_class_name("td_block_inner")
blog_rows = blog_id.find_elements(By.CLASS_NAME,"td-block-row")
for blog_row in blog_rows:
    blocks = blog_row.find_elements(By.CLASS_NAME,"td-block-span6")
    for block in blocks:
        a_tags = block.find_elements(By.TAG_NAME,"a")
        for a_tag in a_tags:
            print(a_tag.get_attribute('title'))
            print(a_tag.get_attribute('href'))

# driver.quit() #to close browser window