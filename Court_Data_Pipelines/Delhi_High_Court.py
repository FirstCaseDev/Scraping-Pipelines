from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Common_Files.Case_pdf_handling import download_Pdf





PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

def page_reader():################# for Reading Contents of page when date is entered ###################
    link = driver.find_element_by_xpath("/html/body/table[2]")
    table = link.find_element_by_xpath("/html/body/table[2]/tbody")
    rows = table.find_elements(By.TAG_NAME, "tr")
    rows.pop()
    for row in rows:
        col = row.find_elements(By.TAG_NAME,"td")
        for c in col:
            a_tags = c.find_elements(By.TAG_NAME,"a")
            for a_tag in a_tags:
                print(a_tag.text)
                print(a_tag.get_attribute('href'))
                download_Pdf(a_tag.get_attribute('href'))
            print(c.text)    

def judgementDate():###############  navigate to JudgementDate Page ####################################
    driver.get("http://164.100.69.66/jsearch/")
    print(driver.title)
    link = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[@class='style13'][3]/b/input[@class='btn']")
    link.click()


def Calendar(D, M,Y, D1, M2, Y2):######  for date iteration to be entered ##############################

    D = int(D)
    M = int(M)
    Y = int(Y)
    D1 = int(D1)
    M2 = int(M2)
    Y2 = int(Y2)

    startm=M
    k=0
    a=""
    date=[]
    while M!=M2 and Y!=Y2 and M<13:
        k=32-D
        q=13-M
        for j in range(q):
            for i in range(k):
                a = str(D+i)+"/"+str(M)+"/"+str(Y)
                date.append(a)

            M=M+1
            M=M%13
        Y = Y+1
    if M==0:
        M=M+1
    while M!=M2 and Y==Y2:
        k= 32-D
        if (M==startm):
            for i in range(k):
                a = str(D+i)+"/"+str(M)+"/"+str(Y)
                date.append(a)
            M=M+1
        else:
            for i in range(k):
                a = str(1+i)+"/"+str(M)+"/"+str(Y)
                date.append(a)
            M=M+1

    if M==0:
        M=M+1
    if M==M2 and Y==Y2:
        k = D1-D
        for i in range(k):
            a = str(D+i)+"/"+str(M)+"/"+str(Y)
            date.append(a)
    # print(w)
    return date
            


D,M,Y = input().split()
D1,M2,Y2 = input().split()
w=Calendar(D,M,Y,D1,M2,Y2)




for i in range(len(w)):
    u = w[i]
    judgementDate()
    try:
        driver.switch_to.frame("dynfr")
        input_box = driver.find_element_by_xpath("//*[@id='juddt']")
        driver.execute_script('document.getElementsByName("juddt")[0].removeAttribute("readonly")')
        input_box.clear()
        input_box.send_keys(u)
        submit_btn = driver.find_element_by_name("Submit")
        submit_btn.click()
        driver.switch_to.default_content()
        
        frame = driver.find_element_by_name("dynfr")############################for grasping data##########
        driver.switch_to.frame(frame)
        page_reader()
        
        try:
            while (driver.find_element_by_link_text("Next").click() == None):
                page_reader()

        except:
            print("This is end of the results.........................") 
    except:
        continue
               












