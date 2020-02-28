from docx import Document

document = Document(
    '/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/latex.docx')
document.save(
    '/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/latex.docx')

import re
line = -1
streetno = {}

# search for cite key word to get references
guestFile = open(
    "/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/References.csv", "w")
guestFile.close()

with open(filepath, errors='ignore') as fp:
    line = fp.readline()
    cnt = 1
    while line:
        if '\section' in line:
            line = line+1
            # print(line)
        if '\cite{' in line:
            # print(paragraph.text)
            text = line
            m = re.findall('{(.+?)}', text)
            for k in m:
                print(k)
                guestFile = open(
                    "/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/References.csv", "a")
                guestFile.write(k)
                guestFile.write("\n")
                line = line+1
                streetno[line] = k
