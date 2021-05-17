from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from Common_Files.Case_pdf_handling import extract_txt
from Common_Files.Case_handler import CaseDoc
from Common_Files.Case_storage import store_case_document
from selenium.webdriver.chrome.options import Options

#setting up the driver
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

PATH='C://Program Files (x86)//chromedriver.exe'
driver= webdriver.Chrome(PATH)
#driver = webdriver.Chrome(PATH,chrome_options=options) #Uncomment only this line for Headless

#opening an instance @Singapore Court
driver.get('https://www.supremecourt.gov.sg/news/supreme-court-judgments')

#page counter
#pg_counter=0

#scrapping page's data
while True:
    case = CaseDoc()
    #pg_counter+=1
    
    #accessing target(ul) 
    target_ul=driver.find_element_by_xpath('/html/body/form/div[4]/section[2]/div/div[2]/div[3]/ul[1]')
    lis=target_ul.find_elements(By.TAG_NAME,'li')

    #counter for elements to be scrapped from a single page
    txt_counter=1

    for li in lis:
        
        #accessing internal div(s)
        if txt_counter<9:
            
            #accessing internal div(s)
            if txt_counter<9:
                
                #accessing target div tag
                txt=li.find_element_by_xpath(str('//*[@id="ContentPlaceHolderContent_C008_DivCode"]/ul[1]/li['+str(txt_counter)+']/div/div[1]'))
                
                #accessing target a tag
                try:
                    a_tag=li.find_element_by_xpath(str('/html/body/form/div[4]/section[2]/div/div[2]/div[3]/ul[1]/li['+str(txt_counter)+']/div/div[2]/a[2]'))
                except:
                    a_tag=li.find_element_by_xpath(str('/html/body/form/div[4]/section[2]/div/div[2]/div[3]/ul[1]/li['+str(txt_counter)+']/div/div[2]/a'))
                    
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
                #print('Petitioner Name :', all_data_str[:indice_2])
                case.petitioner = all_data_str[:indice_2]
                #print('Respondent Name :', all_data_str[indice_2+3:indice_0-1])
                case.respondent = all_data_str[indice_2+3:indice_0-1]
                #excluding pet. and resp. names
                slice_1=all_data_str[all_data_str.find('\n')+1:]
                #Case Title
                case.title=case.petitioner + "  V  " +case.respondent

                #filing date and bench
                indice_3=slice_1.find('[')
                indice_4=slice_1.find(']')
                indice_5=slice_1.find('DECISION')
                
                #print('Filing Date     :', slice_1[indice_3+1:indice_4])
                
                #print('Bench           :', slice_1[indice_4+2:indice_5])
                case.bench = slice_1[indice_4+2:indice_5]
                #excluding f-date & bench
                slice_2=slice_1[indice_5:]

                #decision date
                indice_6=slice_2.find(':')
                #print('Decision Date   :', slice_2[indice_6+2:indice_6+13])
                date = datetime.strptime(slice_2[indice_6+2:indice_6+13],'%d %b %Y')
                case.date = date.strftime('%d-%m-%Y')
                case.day = date.strftime('%d')
                case.month = date.strftime('%B')
                case.year = date.strftime("%Y")
                
                #print('Case number     :',slice_2[indice_6+14:])
                case.case_id = slice_2[indice_6+14:]
                #pdf link
                #print('Pdf link        :',pdf_link)
                case.url = pdf_link



                judgement_text = extract_txt(pdf_link, "SingaporeSupreme.pdf")
                print(len(judgement_text))
                case.judgement_text = judgement_text
                case.source = "Supreme Court Singapore"


                case.process_text()
                case.print_case_attributes()
                store_case_document(case)

                txt_counter+=1
                print()
                print("PAGE Counter :"+ str(pg_counter))
        
            
            #accessing target a tag
            a_tag=li.find_element_by_xpath(str('/html/body/form/div[4]/section[2]/div/div[2]/div[3]/ul[1]/li['+str(txt_counter)+']/div/div[2]/a'))
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
            #print('Petitioner Name :', all_data_str[:indice_2])
            case.petitioner = all_data_str[:indice_2]
            #print('Respondent Name :', all_data_str[indice_2+3:indice_0-1])
            case.respondent = all_data_str[indice_2+3:indice_0-1]
            #excluding pet. and resp. names
            slice_1=all_data_str[all_data_str.find('\n')+1:]

            #filing date and bench
            indice_3=slice_1.find('[')
            indice_4=slice_1.find(']')
            indice_5=slice_1.find('DECISION')
            
            #print('Filing Date     :', slice_1[indice_3+1:indice_4])
            
            #print('Bench           :', slice_1[indice_4+2:indice_5])
            case.bench = slice_1[indice_4+2:indice_5]
            #excluding f-date & bench
            slice_2=slice_1[indice_5:]

            #decision date
            indice_6=slice_2.find(':')
            #print('Decision Date   :', slice_2[indice_6+2:indice_6+13])
            case.date = slice_2[indice_6+2:indice_6+13]
            #print('Case number     :',slice_2[indice_6+14:])
            case.case_id = slice_2[indice_6+14:]
            #pdf link
            print('Pdf link        :',pdf_link)
            judgement_text = extract_txt(pdf_link, "SingaporeSupreme.pdf")
            print(len(judgement_text))
            case.judgement_text = judgement_text
            case.source = "Supreme Court Singapore"
            case.process_text()
            case.print_case_attributes()
            store_case_document(case)
            txt_counter+=1
            print()
    
        
    #clicking next pg button
    driver.find_element_by_xpath('/html/body/form/div[4]/section[2]/div/div[2]/div[3]/div[4]/div[3]/a').click()
    time.sleep(2)
        
       
# for i in range(2000,2022):
#     year = i
#     print(year)
#     #opening an instance @Singapore Court
    # driver.get(f'https://www.supremecourt.gov.sg/news/supreme-court-judgments/year/{year}/page/45')
    # case_scraper()
for i in range(2004,2022):    
    year=i
    driver.get(f'https://www.supremecourt.gov.sg/news/supreme-court-judgments/year/{year}')
    count = int((driver.find_element_by_xpath('/html/body/form/div[4]/section[2]/div/div[2]/div[3]/div[1]/div[2]').text).split("JUDGMENTS")[0])
    print(count)
    Q = (count//8)+1
    print(Q)
    page=Q
    driver.get(f'https://www.supremecourt.gov.sg/news/supreme-court-judgments/year/{year}/page/{page}')
    try:
        case_scraper()
    except:
        print('Done for the year: '+ str(year))    





