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
#path = "mongodb+srv://PuneetShrivas:admin@betatesting.nsnxl.mongodb.net/<dbname>?retryWrites=true&w=majority" #### OLD SERVER LINK
path = "mongodb://db_user:firstCaseDevTeam@54.225.30.33:27017,54.208.244.16:27017,54.198.49.231:27017/?authSource=admin&replicaSet=aName&readPreference=primaryPreferred&ssl=false"

client = pymongo.MongoClient(path)
db = client["article_data"]
col = db["articles"]
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
#PATH = r"C:\\Program Files (x86)\\chromedriver.exe"
PATH = "/root/chromedriver" ## only uncomment when on server
driver = webdriver.Chrome(PATH,chrome_options=options) #Headless
# driver = webdriver.Chrome(PATH) #Windowed
driver.get("https://indconlawphil.wordpress.com/")

while(1):
    blogs = driver.find_elements_by_css_selector(".hentry")
    for blog in blogs: 
        title = blog.find_element_by_css_selector(".entry-title").text
        url = blog.find_element_by_css_selector(".entry-title").find_element_by_tag_name("a").get_attribute("href")
        if(col.find({"url": url}).count()>0):
            print("article already present : "+ str(title))
            continue
        source = "Indian Constitution Law and Philosophy"
        text =  blog.find_element_by_css_selector(".entry-content").text.replace('\n','').replace('\r','')
        acts_list = article_get_acts_list(text)
        cases_list = article_get_cases_list(text)
        article = {"source": source, "text": text, "title": title, "url": url, "acts_list": acts_list, "cases_list": cases_list}
        print(str(col.insert_one(article)))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
