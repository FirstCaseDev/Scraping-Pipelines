from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

PATH = "C:\\Users\\punee\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(PATH,chrome_options=options)
driver.get("https://www.mondaq.com/1/India")
#HANDLER FOR LANDING HOME PAGE
titles = driver.find_elements_by_css_selector("div.title")
titles_list = []
count = 0
for title in titles:
    titles_list.append(title.text)
    a_tag = title.find_element_by_tag_name("a")
    count = count + 1
    # print(a_tag.get_attribute("href"))
    # todo : process links
print("***first page titles: " + str(count) + "***")

# #HANDLER FOR TABULATED ARTICLES
page_number = 2
while(page_number<=3):
    url = "https://www.mondaq.com/1/India/?tab=morenews&pageNumber={0}&order=2".format(page_number) 
    print(url)
    driver.get(url)
    titles_tabulated = driver.find_elements_by_css_selector("td:nth-child(2) a")
    tabulated_titles_count = 0
    for title_tabulated in titles_tabulated:
        titles_list.append(title_tabulated.text)
        # todo : process links
        tabulated_titles_count = tabulated_titles_count + 1
    print("***" + str(page_number) + " table titles: " + str(count) + "***")
    page_number = page_number + 1

driver.quit()
print(titles_list)
print("total tiles : " + str(len(titles_list)))