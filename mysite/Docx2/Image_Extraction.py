#name of the figures
from docx import *
import re
document = Document('/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Sample_2.docx')
guestFile = open("/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Image_Extraction.csv","wb")
guestFile.write("ID".encode("utf-8")+",".encode("utf-8")+"NAME".encode("utf-8")+"\n".encode("utf-8"))
f=0
for para in document.paragraphs:
    if para.text=="Table captions":
        break
    if para.text == "Figure captions":
        f=1
        i=1
        continue
    if len(para.text)>=1 and f==1: 
        s = para.text.replace(",","")
        x = "Figure"+" "+str(i)
        i = i+1
        guestFile.write(x.encode("utf-8")+",".encode("utf-8")+s.encode("utf-8")+"\n".encode("utf-8"))
        print("figures"+para.text)
guestFile.close()
