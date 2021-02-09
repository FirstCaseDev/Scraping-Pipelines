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
driver.get("https://www.mondaq.com/1/India")


#****************************EXTRACTS TEXT FROM ARTICLE****************************
def article_get_text(url):
    script = "window.open('{0}', 'new_window')".format(url)
    driver.execute_script(script)
    driver.switch_to_window(driver.window_handles[-1])
    print(driver.title)
    # WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#articlebody")))
    content = driver.find_element_by_css_selector("#articlebody")
    content_text = content.text
    print(article_get_length(content_text))
    return content_text
    # **************************************Handles pop up*******************************************
    # WebDriverWait(driver,60).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#cd-user-modal")))
    # popup_close = driver.find_element_by_css_selector("#cd-close-form-x")
    # popup_close.click()


#****************************LOGINS ON THE HOME PAGE****************************
login = driver.find_element_by_css_selector(".topnav.cd-signin")
login.click()
email_input = driver.find_element_by_css_selector("#signin-email")
email_input.send_keys("amansingh32@gmail.com")
email_input = driver.find_element_by_css_selector("#signin-password")
email_input.send_keys("admin123")
submit_login = driver.find_element_by_css_selector("#submitLogin")
submit_login.click()


#****************************HANDLER FOR LANDING HOME PAGE****************************
time.sleep(10)
titles = driver.find_elements_by_css_selector("div.title")
titles_list = []
articles = []
count = 0
for title in titles:
    count = count + 1
    title_text = title.text
    a_tag = title.find_element_by_tag_name("a")
    original_handle = driver.window_handles[0]
    url = a_tag.get_attribute("href")
    if(col.find({"url": url}).count()>0):
        print("article already present : "+ str(title_text))
        continue
    text = article_get_text(url)
    for handle in driver.window_handles:
        if(handle!=original_handle):
            driver.switch_to_window(handle)
            driver.close()
    driver.switch_to_window(original_handle)
    cases_list = article_get_cases_list(text)
    acts_list = article_get_acts_list(text)
    article = {"source": "Mondaq", "text": text, "title": title_text, "url": url, "acts_list": acts_list, "cases_list": cases_list}
    print(str(col.insert_one(article)))
    # todo add pymongo handler
print("***first page titles: " + str(count) + "***")



#****************************HANDLER FOR TABULATED ARTICLES****************************
page_number = 2
while(page_number<=50):
    time.sleep(10)
    url = "https://www.mondaq.com/1/India/?tab=morenews&pageNumber={0}&order=2".format(page_number) 
    print(url)
    driver.get(url)
    titles_tabulated = driver.find_elements_by_css_selector("td:nth-child(2) a")
    tabulated_titles_count = 0
    for title_tabulated in titles_tabulated:
        tabulated_titles_count = tabulated_titles_count + 1
        title_text = title_tabulated.text
        # a_tag = title_tabulated.find_element_by_tag_name("a")
        original_handle = driver.window_handles[0]
        url = title_tabulated.get_attribute("href")
        if(col.find({"url": url}).count()>0):
            print("article already present : "+ str(title_text))
        continue
        text = article_get_text(url)
        print(title_text)
        # print(len(text))
        for handle in driver.window_handles:
            if(handle!=original_handle):
                driver.switch_to_window(handle)
                driver.close()
        driver.switch_to_window(original_handle)
        cases_list = article_get_cases_list(text)
        acts_list = article_get_acts_list(text)
        article = {"source": "Mondaq", "text": text, "title": title_text, "url": url, "acts_list": acts_list, "cases_list": cases_list}
        print(str(col.insert_one(article)))
        # todo add pymongo handler
    print("***" + str(page_number) + " table titles: " + str(count) + "***")
    page_number = page_number + 1



#****************************SCRIPT END AND STATS LOGGING****************************
driver.quit()
