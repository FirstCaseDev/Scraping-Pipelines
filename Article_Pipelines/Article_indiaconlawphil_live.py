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
driver.get("https://indconlawphil.wordpress.com/")

while(1):
    blogs = driver.find_elements_by_css_selector(".hentry")
    last_updated_url='x'
    for blog in blogs: 
        title = blog.find_element_by_css_selector(".entry-title").text
        url = blog.find_element_by_css_selector(".entry-title").find_element_by_tag_name("a").get_attribute("href")
        last_updated_url=url
        if(col.find({"url": url}).count()>0):
            print("article already present : "+ str(title))
            break
        source = "Indian Constitution Law and Philosophy"
        text =  blog.find_element_by_css_selector(".entry-content").text.replace('\n','').replace('\r','')
        acts_list = article_get_acts_list(text)
        cases_list = article_get_cases_list(text)
        article = {"source": source, "text": text, "title": title, "url": url, "acts_list": acts_list, "cases_list": cases_list}
        print(str(col.insert_one(article)))

    if(col.find({"url": last_updated_url}).count()>0):
        break
        
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.quit()

