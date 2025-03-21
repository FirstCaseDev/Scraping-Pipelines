from selenium import webdriver
import time
import pymongo
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from Article_extractor import article_get_acts_list, article_get_cases_list, article_get_length
from selenium.webdriver.chrome.options import Options


client = pymongo.MongoClient("mongodb+srv://PuneetShrivas:admin@betatesting.nsnxl.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client["article_data"]
col = db["articles"]

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("--window-size=1280,720")
options.add_argument("--no-sandbox")
#PATH = "C:\\Users\\punee\\Downloads\\chromedriver_win32\\chromedriver.exe"
# driver = webdriver.Chrome(PATH,chrome_options=options) #Headless
PATH='C://Program Files (x86)//chromedriver.exe'
driver = webdriver.Chrome(PATH) #Windowed
driver.get("https://blog.ipleaders.in/blog/")

def article_get_text(url):
    script = "window.open('{0}', 'new_window')".format(url)
    driver.execute_script(script)
    driver.switch_to_window(driver.window_handles[-1])
    text = driver.find_element_by_css_selector(".td-post-content").text
    print(driver.title)
    return text

time.sleep(10)
while(1):
    blogs_section = driver.find_element_by_class_name("td_block_inner")
    blog_rows = blogs_section.find_elements(By.CLASS_NAME,"td-block-row")
    for blog_row in blog_rows:
        blocks = blog_row.find_elements(By.CLASS_NAME,"td-block-span6")
        last_updated_url='x'

        for block in blocks:
            a_tag = block.find_element(By.TAG_NAME,"a")
            title = a_tag.get_attribute('title')
            url = a_tag.get_attribute('href')
            last_updated_url=url

            if(col.find({"url": url}).count()>0):
                print("article already present : "+ str(title))
                break

            original_handle = driver.window_handles[0]
            text = article_get_text(url).replace('\n','').replace('\r','')
            source = "IPleaders"
            for handle in driver.window_handles:
                if(handle!=original_handle):
                    driver.switch_to_window(handle)
                    driver.close()
                    
            driver.switch_to_window(original_handle)
            print(article_get_length(text))
            cases_list = article_get_cases_list(text)
            acts_list = article_get_acts_list(text)
            article = {"source": source, "text": text, "title": title, "url": url, "acts_list": acts_list, "cases_list": cases_list}
            print(str(col.insert_one(article)))

    if(col.find({"url": last_updated_url}).count()>0):
        break

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.quit() #to close browser window

# WebDriverWait(driver,120).until(EC.visibility_of_element_located((By.CLASS_NAME,"popautoscroll")))
# close_overlay = driver.find_element_by_xpath("//*[@id='shwPopsCls']")
# close_overlay.click()
# WebDriverWait(driver,10).until(presence_of_all_elements_located((By.ID,"td_block_inner")))
