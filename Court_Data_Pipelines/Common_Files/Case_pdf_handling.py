########################  Downloading Pdf Files ########################
import requests



def download_Pdf(a):
    url = a
    r = requests.get(url)
    filename = r.url[url.rfind('/')+1:]
    print(filename)
    open(filename, 'wb').write(r.content)

#######################################################################

#######################################################
##### Using Pdfminer Pdf to text converter ##########################
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt



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
			
# initial_Dir = (r"C:\\Users\\Pushpak\\Documents\\First_case\\pdf\\")
# Final_Dir = (r"C:\\Users\\Pushpak\\Documents\\First_case\\text\\")
# Pdf2Conv(initial_Dir, Final_Dir)
# print("Pdf saved")

#####################################################################################


