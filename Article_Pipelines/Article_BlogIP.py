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
# WebDriverWait(driver,120).until(EC.visibility_of_element_located((By.CLASS_NAME,"popautoscroll")))
# close_overlay = driver.find_element_by_xpath("//*[@id='shwPopsCls']")
# close_overlay.click()
# WebDriverWait(driver,10).until(presence_of_all_elements_located((By.ID,"td_block_inner")))
# while(true):
last_count = 0
while(1):
    count = 0
    blog_id = driver.find_element_by_class_name("td_block_inner")
    blog_rows = blog_id.find_elements(By.CLASS_NAME,"td-block-row")
    for blog_row in blog_rows:
        count = count + 1
        if(count<last_count): continue
        last_count = count
        print("count : "+ str(count))
        print("lastcount : "+ str(last_count))
        blocks = blog_row.find_elements(By.CLASS_NAME,"td-block-span6")
        for block in blocks:
            a_tag = block.find_element(By.TAG_NAME,"a")
            # print(a_tag.get_attribute('title'))
            # print(a_tag.get_attribute('href'))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def get_article(url):
    script = "window.open('{0}', 'new_window')".format(url)
    driver.execute_script(script)
    driver.switch_to_window(driver.window_handles[-1])
    print(driver.title)

# driver.quit() #to close browser window