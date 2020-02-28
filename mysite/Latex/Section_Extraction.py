from docx import Document
#reading latex file
document = open('/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/latex.txt','r')
#document.save('/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/latex.docx')

import re
filepath = '/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/latex.txt'
dictlabel={}
c=0
guestFile = open("/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/SectionExtraction.csv","w")
guestFile.close()
with open(filepath,errors='ignore') as fp:
       line = fp.readline()
       while line:
          #  print(line)
            if 'section{' in line and '\label{' in line: 
                    m = re.findall('{(.+?)}', line)
                    dictlabel[m[1].lower().replace(" ","")] = c    
                    c = c+1
            line = fp.readline()
            
print(dictlabel)
for i in dictlabel:
    guestFile = open("/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/SectionExtraction.csv","a")
    guestFile.write(i)
    print(i)
    guestFile.write("\n")
    guestFile.close()
	
	
