#figure names
from docx import *
import re
from pathlib import Path
import os

CUR_BASE_DIR = os.path.join("/home/kushal/Desktop/MTP_project/Django_MTP" ,"mysite", "media2")

document = Document(os.path.join(CUR_BASE_DIR, 'Sample_1.docx'))
section=""
figure_name = ""
guestFileName = os.path.join(CUR_BASE_DIR, 'Section_Image.csv')
guestFile = open(guestFileName,"wb")
guestFile.write("Section id".encode("utf-8")+",".encode("utf-8"))
guestFile.write("Section name".encode("utf-8")+",".encode("utf-8"))
guestFile.write("Image".encode("utf-8")+"\n".encode("utf-8"))
for para in document.paragraphs:
    f2=0
    f1=0
    f3=0
    x1=""
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
    if len(para.text)>=1:
       # print(para.text)
        str = para.text.split(' ')
        for s in str:
            if f3==1:
                figure_name.append(s)
                f3 = 0
                print(section,figure_name)
                guestFile = open(guestFileName,"ab")
                for s2 in section.split(" "):
                        guestFile.write(s2.encode("utf-8")+",".encode("utf-8"))
                guestFile.write(figure_name[0].encode("utf-8")+" ".encode("utf-8")+figure_name[1].replace(")","").replace(".","").encode("utf-8"))
                guestFile.write("\n".encode("utf-8"))
                guestFile.close()
            x1 = re.findall("figure", s)
            if len(x1)>=1:
                figure_name = x1
                f3 = 1
    if f2!=1 and x:
        section = para.text.strip()
        #print(x,y)
        f2=0
