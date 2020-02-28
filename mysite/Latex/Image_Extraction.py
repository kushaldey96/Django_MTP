from docx import Document

document = Document('/home/kushal/Desktop/MTP_project/Django_code/mysite/Latex/latex.docx')
document.save('/home/kushal/Desktop/MTP_project/Django_code/mysite/Latex/latex.docx')

import re
import csv

#extracting images form based on include graphics
    
flag=0    
for paragraph in document.paragraphs:
    if 'includegraphics' in paragraph.text:
       ## print(paragraph.text)
        text = paragraph.text
        m = re.search('{(.+?)}', text)
        print(m.group(1))
        s = m.group(1)
        if flag == 1:
            with open('/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/ImageNames.csv', 'a') as f:
                for line in s:
                    f.write(line)
                    flag = 1
                f.write("\n")    
        else:        
            with open('/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/ImageNames.csv', 'w') as f:
                for line in s:
                    f.write(line)
                    flag = 1;
                f.write("\n")            
				
import re
filepath = '/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/latex.txt'
f=0
out={}
flag = 0
#printing section and image names within section

with open(filepath,errors='ignore') as fp:
       line = fp.readline()
       cnt = 1
       while line:
          #  print(line)
            if '\section{' in line:
                if '\label{' in line:
                    f = 1   
                    m = re.findall('{(.+?)}', line)
                  #  print("ff")
                    print(m[0])   
                    s = m[0]
                 #  print(line)
            if 'includegraphics' in line:
                m1 = re.findall('{(.+?)}', line)
                if len(m1)!=0:
                  #  print(m[0])
                    for k in m1:
                        tuples = m[0],k
                        if tuples in out.keys():
                            out[m[0],k] = out[m[0],k] + 1
                            
                        else:    
                            out[m[0],k] = 1
                    print(m1)
                    s = m1
                    f=0;
            line = fp.readline()
            cnt += 1
           
print(out)
guestFile = open("/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Section_Image_Correlation.csv","w")
guestFile.close()
for entries in out :
    guestFile = open("/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Section_Image_Correlation.csv","a")
    s = entries[0]+","+entries[1]+","+str(out.get(entries))
    guestFile.write(s)
    print(s)
    guestFile.write("\n")
    guestFile.close()

import operator
from operator import itemgetter

#counting section and image references
guestFile = open("/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Section_Image_Correlation_sorted.csv","w")
guestFile.close()
out1 = dict(sorted(out.items(),key=operator.itemgetter(1),reverse=True))
sorted(out.items(),key=operator.itemgetter(1),reverse=True)
for entries in out1 :
    guestFile = open("/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Section_Image_Correlation_sorted.csv","a")
    s = entries[0]+","+entries[1]+","+str(out.get(entries))
    guestFile.write(s)
    print(s)
    guestFile.write("\n")
    guestFile.close()
#print(out1)

	
