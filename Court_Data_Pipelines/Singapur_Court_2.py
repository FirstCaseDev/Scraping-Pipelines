from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located


#setting up the driver

PATH='C://Program Files (x86)//chromedriver.exe'
driver= webdriver.Chrome(PATH)

#opening an instance @Singapore Court
driver.get('https://www.supremecourt.gov.sg/news/supreme-court-judgments')

#page counter
#pg_counter=0

#scrapping page's data
while True:
    
    #pg_counter+=1
    
    #accessing target(ul) 
    target_ul=driver.find_element_by_xpath('/html/body/form/div[4]/section[2]/div/div[2]/div[3]/ul[1]')
    lis=target_ul.find_elements(By.TAG_NAME,'li')

    #counter for elements to be scrapped from a single page
    txt_counter=1

    for li in lis:
        
        #accessing internal div(s)
        if txt_counter<9:
            
            #accessing target div tag
            txt=li.find_element_by_xpath(str('//*[@id="ContentPlaceHolderContent_C008_DivCode"]/ul[1]/li['+str(txt_counter)+']/div/div[1]'))
            
            #accessing target a tag
            #a_tag=li.find_element_by_xpath(str('/html/body/form/div[4]/section[2]/div/div[2]/div[3]/ul[1]/li['+str(txt_counter)+']/div/div[2]/a'))
            a_tag = li.find_element(By.CLASS_NAME,'pdf-download')
            pdf_link=a_tag.get_attribute('href')

            temp_list=[]
            temp_list.append(txt.text)
            temp_str=temp_list[0]
            indice_1=temp_str.find('\n')
            
            all_data_str=temp_str[indice_1+1:]
            
            #slicing string according to the entry fields
            
            #Petioner-name and respondent-name
            indice_2=all_data_str.find(' v ')
            indice_0=all_data_str.find('[')    
            print('Petitioner Name :', all_data_str[:indice_2])
            print('Respondent Name :', all_data_str[indice_2+3:indice_0-1])

            #excluding pet. and resp. names
            slice_1=all_data_str[all_data_str.find('\n')+1:]

            #filing date and bench
            indice_3=slice_1.find('[')
            indice_4=slice_1.find(']')
            indice_5=slice_1.find('DECISION')
            
            print('Filing Date     :', slice_1[indice_3+1:indice_4])
            print('Bench           :', slice_1[indice_4+2:indice_5])
            
            #excluding f-date & bench
            slice_2=slice_1[indice_5:]

            #decision date
            indice_6=slice_2.find(':')
            print('Decision Date   :', slice_2[indice_6+2:indice_6+13])

            print('Case number     :',slice_2[indice_6+14:])

            #pdf link
            print('Pdf link        :',pdf_link)
<<<<<<< Updated upstream

=======
            judgement_text = extract_txt(pdf_link, "SingaporeSupreme.pdf")
            print(len(judgement_text))
            case.judgement_text = judgement_text
            case.source = "Supreme Court Singapore"
            #case.process_text()
            case.print_case_attributes()
            #store_case_document(case)
>>>>>>> Stashed changes
            txt_counter+=1
            print()
    
        
    #clicking next pg button
    driver.find_element_by_xpath('/html/body/form/div[4]/section[2]/div/div[2]/div[3]/div[4]/div[3]/a').click()
    time.sleep(2)
        
        






