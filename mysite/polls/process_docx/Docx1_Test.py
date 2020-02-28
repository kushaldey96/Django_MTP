import os
import shutil
import glob, os


program_dir = os.path.join("/home/kushal/Desktop/MTP_project/Django_MTP/mysite/polls/process_docx/")
csv_dir = os.path.join("/home/kushal/Desktop/MTP_project/Django_MTP/mysite/media2/")
upload_dir = os.path.join("/home/kushal/Desktop/MTP_project/Django_MTP/mysite/media/")


'''d = '/home/kushal/Desktop/MTP_project/Django_code/mysite/media2'
filesToRemove = [os.path.join(d,f) for f in os.listdir(d)]
for f in filesToRemove:
    os.remove(f) '''
arr = os.listdir(upload_dir)
x = upload_dir + arr[0]
txt_file = csv_dir + 'Sample_1.txt'
docx_file = csv_dir + 'Sample_1.docx'
shutil.copy2(x, txt_file)
shutil.copy2(x, docx_file)
print(arr)

