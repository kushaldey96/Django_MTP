#section and images correlation
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
guestFile = open("Section_Table.csv","w")
guestFile.write("Section Id"+",")
guestFile.write("Section name"+",")
guestFile.write("Table Name"+"\n")
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
                guestFile = open("Section_Table.csv","a")
                f4 = 0;
                for s2 in section.split(" "):
                    if f4 == 1:
                        guestFile.write(",")
                    f4 = f4+1
                    guestFile.write(s2+" ")
                s3 = ""
                guestFile.write(",")
                for s2 in figure_name:
                    s3 = s3 + s2;
                guestFile.write(s3.replace(",","").replace(".",""))
                guestFile.write("\n")
                guestFile.close()
            x1 = re.findall("Table", s)
            if len(x1)>=1:
                figure_name = x1
                f3 = 1
    if f2!=1 and x:
        section = para.text.strip()
        #print(x,y)
        f2=0
