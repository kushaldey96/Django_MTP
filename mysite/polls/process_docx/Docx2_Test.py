import os
import shutil
arr = os.listdir('/home/kushal/Desktop/MTP_project/Django_code/mysite/media')
x = '/home/kushal/Desktop/MTP_project/Django_code/mysite/media/' + arr[0]
shutil.copy2(x, '/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Sample_2.txt')
shutil.copy2(x, '/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Sample_2.docx')
print(arr)

