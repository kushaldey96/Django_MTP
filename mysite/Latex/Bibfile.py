from docx import Document

document = Document('/home/kushal/Desktop/MTP_project/Django_code/mysite/Latex/latex.docx')
'''document.save('/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/latex.docx')
'''
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode
#bib file parsing
with open('/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/bibtex.bib') as bibtex_file:
    parser = BibTexParser()
    parser.customization = convert_to_unicode
    bib_database = bibtexparser.load(bibtex_file, parser=parser)
    print(bib_database.entries)
  
	
import csv
data = bib_database.entries
print(data)
#writing in csv file
with open('/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/bibfile.csv', 'w') as csvFile:
    fields = ['year','journal','author','title']
    writer = csv.DictWriter(csvFile, fieldnames=fields,extrasaction='ignore')
    writer.writeheader()
    writer.writerows(data)
csvFile.close()

map1={}
for i in bib_database.entries:
    val = i.get('year')
    if val in map1.keys():
        map1[i.get('year')] = map1[i.get('year')] + 1
    else:
        map1[i.get('year')] = 1
print(map1)    

from heapq import nlargest
y_axis = []
x_axis = []
print(map1)
for val in map1.keys(): 
    print(val," ",map1[val])
    y_axis.append(map1[val])
    x_axis.append(val)

	
