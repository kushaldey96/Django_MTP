import os
import shutil
arr = os.listdir('/home/kushal/Desktop/MTP_project/Django_code/mysite/media')
#os.rename(latex.docx, 'Sample_1.txt')
x = '/home/kushal/Desktop/MTP_project/Django_code/mysite/media/' + arr[0]
y = '/home/kushal/Desktop/MTP_project/Django_code/mysite/media/' + arr[1]
if ".bib" in x:
    shutil.copy2(
        x, '/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/bib.txt')
    shutil.copy2(
        x, '/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/bibtex.bib')
    shutil.copy2(
        y, '/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/latex.docx')
    shutil.copy2(
        y, '/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/latex.txt')
else:
    shutil.copy2(
        y, '/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/bib.txt')
    shutil.copy2(
        y, '/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/bibtex.bib')
    shutil.copy2(
        x, '/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/latex.docx')
    shutil.copy2(
        x, '/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/latex.txt')
