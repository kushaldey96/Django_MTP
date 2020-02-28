import re
filepath = '/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/latex.txt'
f=0

#searching for table keyword

with open(filepath,errors='ignore') as fp:
       line = fp.readline()
       cnt = 1
       while line:
          #  print(line)
            if '\\begin{table' in line:    
                f = 1  
            if '\end{table' in line:    
                f = 0  
            if f==1:
                if '\caption{' in line:
                    m = re.findall('{(.+?)}', line)
                    print(m)
                    f=0;
            line = fp.readline()
            cnt += 1
			
			
import re
filepath = '/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/latex.txt'
f=0
out={}

#searching for section and their names

with open(filepath,errors='ignore') as fp:
       line = fp.readline()
       cnt = 1
       while line:
          #  print(line)
            if '\section{' in line:
                if '\label{' in line: 
                    m = re.findall('{(.+?)}', line)
                  #  print("ff")
                    print(m[0]) 
            if '\\begin{table' in line:    
                f = 1  
            if '\end{table' in line:    
                f = 0   
            if f==1:
                if '\caption{' in line:
                    f=0
                    m1 = re.findall('{(.+?)}', line)
                  #  print("gg",m1)
                    if len(m1)!=0:
                       # print(m1)
                        for k in m1:
                            tuples = m[0],k
                            if tuples in out.keys():
                                out[m[0],k] = out[m[0],k] + 1
                            
                            else:    
                                out[m[0],k] = 1  
            line = fp.readline()
            cnt += 1

import operator
from operator import itemgetter
out1 = dict(sorted(out.items(),key=operator.itemgetter(1),reverse=True))
sorted(out.items(),key=operator.itemgetter(1),reverse=True)
#print(out1)
guestFile = open("/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Table_Section_Correlation.csv","w")
guestFile.close()
out1 = dict(sorted(out.items(),key=operator.itemgetter(1),reverse=True))
for entries in out1 :
    guestFile = open("/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Table_Section_Correlation.csv","a")
    s = entries[0]+","+entries[1]+","+str(out.get(entries))
    guestFile.write(s)
    print(s)
    guestFile.write("\n")
    guestFile.close()

	
