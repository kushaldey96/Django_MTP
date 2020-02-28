#name of the sections
from docx import *
import re
import os
#f = open("demofile1.txt", "r")
#p = f.read()
#print(p)
from pathlib import Path

CUR_BASE_DIR = os.path.join("/home/kushal/Desktop/MTP_project/Django_MTP" ,"mysite", "media2")

document = Document(os.path.join(CUR_BASE_DIR, 'Sample_1.docx'))
print("Introduction")

guestFileName = os.path.join(CUR_BASE_DIR, 'Section.csv')
guestFile = open(guestFileName,"wb")
guestFile.write("Section id".encode("utf-8")+",".encode("utf-8"))
guestFile.write("Section name".encode("utf-8")+"\n".encode("utf-8"))

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
        guestFile = open(guestFileName,"ab")
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
