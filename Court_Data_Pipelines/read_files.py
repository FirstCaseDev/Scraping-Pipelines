from selenium import webdriver
import datefinder
import re
import string
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from Common_Files.Case_handler import CaseDoc
from Common_Files.Case_storage import store_case_document, case_exists_by_url
from datetime import date, timedelta , datetime
from selenium.webdriver.support.ui import Select
import time
case = CaseDoc()

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
PATH = r"C:\\Program Files (x86)\\chromedriver.exe"
#PATH = "/root/chromedriver" ## only uncomment when on server
# driver = webdriver.Chrome(PATH,chrome_options=options) #Uncomment only this line for Headless
driver = webdriver.Chrome(PATH) #Uncomment only this line for Windowed


file1 = open("indian_kanoon_missed_400above_urls.txt","r+") 
lines = file1.readlines()

def process_IndKanoon_case_url(url):
    case = CaseDoc()
    # driver.get(url)
    script = "window.open('{0}', 'case_window')".format(url)
    driver.execute_script(script)
    original_case_handle = driver.window_handles[-2]
    driver.switch_to_window(driver.window_handles[-1])
    driver.set_page_load_timeout(60)
    try:
        try:
            source = driver.find_element_by_css_selector(".docsource_main").text
        except TimeoutException:
            print(url + " was partially loaded")
        try:
            judgement_div = driver.find_element_by_css_selector(".judgments")
        except NoSuchElementException: 
            print("no judgement")
        try:
            author = driver.find_element_by_css_selector(".doc_author").text.split(':')[-1].translate(str.maketrans('', '', string.punctuation)).strip()
        except NoSuchElementException:
            print("no author found")
        try:
            bench = driver.find_element_by_css_selector(".doc_bench").text.split(':')[-1].split(',')
            if '[' in bench[0]:
                bench = re.findall("\[(.*?)\]", bench[0])
        except NoSuchElementException:
            print("no bench found")
        try:
            title = driver.find_element_by_css_selector(".doc_title").text
        except NoSuchElementException:
            print("no title found")
        try:
            source = driver.find_element_by_css_selector(".docsource_main").text
        except NoSuchElementException:
            print("no source found")
        try:
            query_terms_elements = driver.find_elements_by_css_selector(".item_toselect")
            for query_terms_element in query_terms_elements:
                case.query_terms.append(query_terms_element.text)  
        except NoSuchElementException:
            print("no query terms found")
        try:
            p_tags = judgement_div.find_elements_by_css_selector("blockquote, p")
            pre_tags = judgement_div.find_elements_by_tag_name("pre")
        except NoSuchElementException:
            pass
        pre_text = ""
        for pre_tag in pre_tags:
            pre_text = pre_text + "\n\n" + pre_tag.text
        pre_text_splitted = pre_text.replace('ACT:','>>>').replace('HEADNOTE:','>>>').replace('CITATION:','>>>').replace('JUDGEMENT:','>>>').split('>>>')
        paragraphs = p_tags[1:]
        judgement_text_paragraphs = []
        judgement_text_paragraphs.append(pre_text_splitted[0])
        for paragraph in paragraphs:
            judgement_text_paragraphs.append(paragraph.text.replace('\n','').replace('\r','').replace('',''))
        case.judgement_text = ' >>>> '.join(judgement_text_paragraphs)
        dates = datefinder.find_dates(title)
        for i in dates:
            date = i
        case.title = title
        print(case.title)
        try:
            case.petitioner = title.split(' vs ')[0].translate(str.maketrans('', '', string.punctuation)).strip()
        except:
            print("Not FOund")
        try:
            case.respondent = title.split(' vs ')[1].split(' on ')[0]
        except:
            print("Not FOund")
        try:
            case.date = date
            case.year = date.strftime("%Y")
            case.month = date.strftime("%B")
            case.day = date.strftime("%d")
        except:
            print("Not FOund")
        try:
            case.url = url
        except:
            print("Not FOund")
        try:
            case.doc_author = author
        except:
            print("Not FOund")
        try:
            case.bench = bench
        except:
            print("Not FOund")
        try:
            case.source = source
        except:
            print("Not FOund")
        case.process_text() 
        store_case_document(case) #VERY DANGEROUS!!! DON'T UNCOMMENT UNLESS STORING TO DATABASE
        case.print_case_attributes()
    except Exception as inst:
        print(inst)
        open("indian_kanoon_missed_urls.txt", 'a+').write("%s\n" %(url) )
        print("Missed : %s\n" %(url) + (datetime.now().strftime("%m/%d/%Y, %H:%M:%S")) )
   
    driver.close()
    driver.switch_to_window(original_case_handle) 
    return case

def process_IndKanoon_missed_url_by_month_url(url):
    source = url.split("doctypes:")[1].split("%20fromdate:")[0]
    f_date = url.split("fromdate:")[1].split("%20todate")[0]
    t_date = url[::-1].split("02%")[0][::-1]
    
    link = driver.get(url)
    for i in range(41):

        date = datetime.strptime(f_date,'%d-%m-%Y')
        startdate = date
        nextdate = startdate + timedelta(days=1)
        t_date = nextdate.strftime("%d-%m-%Y")
        
        

        searchbox = driver.find_element_by_xpath('//*[@id="search-box"]')
        searchbox.clear()
        searchbox.send_keys(f"doctypes: {source} fromdate: {f_date} todate: {t_date} sortby: leastrecent")
        submit = driver.find_element_by_xpath('//*[@id="submit-button"]').click()
        try:
            total_case_mentioned = int(driver.find_element_by_css_selector("b:nth-child(1)").text.split('of')[-1])
            # print("Total Cases: " + str(total_case_mentioned))
            case_count_in_table = 0
            found_next_page = True
            while(found_next_page):
                case_tags = driver.find_elements_by_css_selector(".result_title a")
                case_count_in_table = case_count_in_table + len(case_tags)
                current_count = 1
                for case_tag in case_tags:
                    case_url = case_tag.get_attribute("href")
                    print("...#" + str(current_count) + " of total " + str(total_case_mentioned) + "cases...")
                    if case_exists_by_url(case_url) == 1:
                        print("case exist")
                    else:
                        process_IndKanoon_case_url(case_url)
                        current_count = current_count + 1
                try:
                    next_page_tag_url = driver.find_element_by_css_selector(".pagenum+ a").get_attribute("href")
                    driver.get(next_page_tag_url)
                except NoSuchElementException:
                    print("...cases missed in scraping :" + str(total_case_mentioned - case_count_in_table))
                    found_next_page = False
        except ValueError :
            print("No Case This Month.")
        

        f_date = t_date

    




for i in range(len(lines)):
    url = lines[i]
    print(url)
    process_IndKanoon_missed_url_by_month_url(url)
    

