#name of the sections
from docx import *
import re
document = Document('/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Sample_2.docx')
print("Introduction")
guestFile = open("/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Section_Extraction.csv","wb")
guestFile.write("ID".encode("utf-8")+",".encode("utf-8"))
guestFile.write("Name".encode("utf-8")+"\n".encode("utf-8"))
f = 0
for para in document.paragraphs:
    f2=0
    f1=0
    if para.text=="":
        continue
    for run in para.runs:
        if run.bold :
            f1=1
        else:
            f2=1
    #print(para.text) 
    if len(para.text)>=1:
       # print(para.text) 
        str = para.text.split(' ')[0]
        x = re.findall("^[0-9][.]", str)
       # if f2!=1:
          #  print(str,x)        
    if f2!=1 and x:
        print(para.text.strip())
        s = para.text.strip().encode("utf-8")
        guestFile = open("/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Section_Extraction.csv","ab")
        s1 = para.text.strip().split(" ")
        f=0
        for s2 in s1:
            if f==1:
                guestFile.write(",".encode("utf-8"))
            f = f+1
            if s2[len(s2)-1]=='.':
                s2 = s2[:len(s2)-1]
            guestFile.write(s2.encode("utf-8"))
        guestFile.write("\n".encode("utf-8"))
        guestFile.close()
        #print(x,y)
        f2=0
