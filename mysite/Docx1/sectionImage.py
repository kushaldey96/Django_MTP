#figure names
from docx import *
import re
from pathlib import Path

data_folder = Path(r"")
file_to_open = data_folder / "newfile2.txt"

f = open(file_to_open)
p = f.read()
print(p)
document = Document(p)
section=""
figure_name = ""
guestFile = open("Section_Image.csv","wb")
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
                guestFile = open("Section_Image.csv","ab")
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
