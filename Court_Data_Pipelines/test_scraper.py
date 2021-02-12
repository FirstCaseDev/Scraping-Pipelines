from Common_Files.Case_handler import CaseDoc
from Common_Files.Case_pdf_handling import extract_txt
case = CaseDoc()
case.judgement_text = extract_txt(r"https://main.sci.gov.in/supremecourt/2007/1677/1677_2007_36_1501_26135_Judgement_12-Feb-2021.pdf","xyz.pdf")
print(case.judgement_text)
# case.process_text()

# print("judgement : "  + str(case.judgement))
# print("petitioner counsel : "  + str(case.petitioner_counsel))
# print("respondent counsel : "  + str(case.respondent_counsel))
# print("cases cited : " + str(case.cases_cited))
# print("provisions referred : " + str(case.provisions_referred))