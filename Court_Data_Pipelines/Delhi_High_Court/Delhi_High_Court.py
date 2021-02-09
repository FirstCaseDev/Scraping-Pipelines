from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://164.100.69.66/jsearch/")
print(driver.title)
link = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[@class='style13'][3]/b/input[@class='btn']")
link.click()

driver.switch_to.frame("dynfr")
input_box = driver.find_element_by_xpath("//*[@id='juddt']")
driver.execute_script('document.getElementsByName("juddt")[0].removeAttribute("readonly")')
input_box.clear()
input_box.send_keys("03/02/2021")
submit_btn = driver.find_element_by_name("Submit")
submit_btn.click()
driver.switch_to.default_content()

frame = driver.find_element_by_name("dynfr")
driver.switch_to.frame(frame)

link = driver.find_element_by_xpath("/html/body/table[2]")
table = link.find_element_by_xpath("/html/body/table[2]/tbody")
rows = table.find_elements(By.TAG_NAME, "tr")
rows.pop()#for removing the last row element 
for row in rows:
    col = row.find_elements(By.TAG_NAME,"td")
    for c in col:
        a_tags = c.find_elements(By.TAG_NAME,"a")
        for a_tag in a_tags:
            print(a_tag.text)
            print(a_tag.get_attribute('href'))
        print(c.text)



