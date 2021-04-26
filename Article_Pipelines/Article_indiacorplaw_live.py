from selenium import webdriver
import time
import pymongo
from Article_extractor import article_get_acts_list, article_get_cases_list, article_get_length
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.chrome.options import Options

client = pymongo.MongoClient("mongodb+srv://PuneetShrivas:admin@betatesting.nsnxl.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client["article_data"]
col = db["articles"]
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
PATH = "C:\\Users\\punee\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(PATH,chrome_options=options) #Headless
# driver = webdriver.Chrome(PATH) #Windowed

def article_get_text(url):
    script = "window.open('{0}', 'new_window')".format(url)
    driver.execute_script(script)
    driver.switch_to_window(driver.window_handles[-1])
    try: 
        text = driver.find_element_by_css_selector(".clearfix").text
        print(article_get_length(text))
    except:
        print("cant get text")    
    print(driver.title)
    return text


page_number = 1
while(1):
    url = "https://indiacorplaw.in/page/{0}".format(page_number)
    driver.get(url)
    blogs = driver.find_elements_by_css_selector(".category-uncategorized")
    last_updated_url='x'
    for blog in blogs:
        title = blog.find_element_by_css_selector(".h1 a").text
        url = blog.find_element_by_css_selector(".entry-footer").find_element_by_tag_name("a").get_attribute("href")
        last_updated_url=url
        
        if(col.find({"url": url}).count()>0):
            print("article already present : "+ str(title))
            break
        source = "IndianCorpLaw"
        original_handle = driver.window_handles[0]
        text = article_get_text(url).replace('\n','').replace('\r','')
        for handle in driver.window_handles:
            if(handle!=original_handle):
                driver.switch_to_window(handle)
                driver.close()
        driver.switch_to_window(original_handle)
        cases_list = article_get_cases_list(text)
        acts_list = article_get_acts_list(text)
        print(title)
        article = {"source": source, "text": text, "title": title, "url": url, "acts_list": acts_list, "cases_list": cases_list}
        print(str(col.insert_one(article)))

    if(col.find({"url": last_updated_url}).count()>0):
        break

    page_number = page_number + 1

driver.quit()

    