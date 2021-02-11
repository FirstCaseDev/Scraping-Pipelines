# # import requests
# import os


# def Pdf2dwnld(a,b):
#     url = a
#     r = requests.get(url)
#     filename = b
#     print(filename)
#     open(filename, 'wb').write(r.content)
########################################################################
# import PyPDF2



# def extract_information(pdf_path):
#     with open(pdf_path, 'rb') as f:
#         Pdfread =PyPDF2.PdfFileReader(f)
#         x=Pdfread.numPages
#         pageobj=Pdfread.getPage(0)
#         text = pageobj.extractText()
#         file1=open(r"C:\Users\Pushpak\Documents\First_case\date.txt","a")
#         file1.writelines(text)
#         file1.close()
#     print("done")
#     return 
#######################################################
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt

##### Using Pdfminer##########################




def extract_txt(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text 




def Pdf2Conv(initial_Dir, Final_Dir):
    if initial_Dir == "": initial_Dir = os.getcwd() + "\\" 
    for pdf in os.listdir(initial_Dir): 
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = initial_Dir + pdf 
            text = extract_txt(pdfFilename) 
            textFilename = Final_Dir + pdf + ".txt"
            textFile = open(textFilename, "w") #make text file
            textFile.write(text) #write text to text file
			
initial_Dir = (r"C:\\Users\\Pushpak\\Documents\\First_case\\pdf\\")
Final_Dir = (r"C:\\Users\\Pushpak\\Documents\\First_case\\text\\")
Pdf2Conv(initial_Dir, Final_Dir)
print("Pdf saved")
# extract_information(r"C:\\Users\\Pushpak\\Documents\\First_case\\my.pdf")
#####################################################################################
# os.system('pdf2txt.py -o pdf2txt.txt my.pdf')
# with open(r'C:\Users\Pushpak\Documents\First_case\New folder\pdf2txt.txt', encoding="utf8") as file:
#     data_txt = file.read()
#     print(data_txt)

#############################PDF
# import os
# os.system('pdf2txt.py -o pdf2html.html -t html xyz.pdf')
# os.system('pdf2txt.py -o pdf2text.txt xyz.pdf')

# with open('new-output.html', encoding="utf8") as file:
#     data_html = file.read()
#     print(data_html)

# with open('pdf2text.txt', encoding="utf8") as file:
#     data_txt = file.read()
#     print(data_txt)

##############Downloading Pdf Files    
# import requests
# for i in range(len(k)):
#     url = k[i]
#     r = requests.get(url)
#     filename = r.url[k[i].rfind('/')+1:]
#     print(filename)
#     open(filename, 'wb').write(r.content)

# print("Download Completed")
# ##########################################