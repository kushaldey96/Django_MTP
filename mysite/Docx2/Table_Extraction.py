#name of the tables
from docx import *
import re
document = Document('/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Sample_2.docx')
guestFile = open("/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/table_Extraction.csv","wb")
guestFile.write("Table Id".encode("utf-8")+",".encode("utf-8"))
guestFile.write("Table Name".encode("utf-8")+"\n".encode("utf-8"))
f=0
for para in document.paragraphs:
    if para.text == "Table captions":
        f=2
        i=1
        continue
    if len(para.text)>=1 and f==2:
        s = para.text.replace(",","-")
        x = "Table"+" "+str(i)
        i = i+1
        guestFile.write(x.encode("utf-8")+",".encode("utf-8")+s.encode("utf-8")+"\n".encode("utf-8"))
        print("tables"+s)
guestFile.close()   
