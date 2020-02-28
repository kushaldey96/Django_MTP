from django.shortcuts import render

from django.http import HttpResponse

import pandas as pd

from django_tables2.tables import Table

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from wsgiref.util import FileWrapper

import os
import shutil
import glob, os
import csv


# Create your views here.

program_dir = os.path.join("/home/kushal/Desktop/MTP_project/Django_MTP/mysite/polls/process_docx")
csv_dir = os.path.join("/home/kushal/Desktop/MTP_project/Django_MTP/mysite/media2")
upload_dir = os.path.join("/home/kushal/Desktop/MTP_project/Django_MTP/mysite/media")

def index(request):
    return render(request,'home.html',{'name':'Kushal'})

def convert(lst):
    return ' '.join(lst)

def upload(request):
    context = {}
#   if request.method == 'GET':
    uploaded_file = request.FILES['document']
    print(uploaded_file.name)
    print(uploaded_file.size)
    print("gg")
    fs = FileSystemStorage()
    name = fs.save(uploaded_file.name, uploaded_file)
#    context['url'] = fs.url(name)
    #print("ggg")
    return render(request, 'upload.html', context)


'''def upload(request):
    context = {}
    print("jj")
    return render(request, 'upload.html', context)'''

def docx1(request):
    # d = '/home/kushal/Desktop/MTP_project/Django_code/mysite/media2'
    docx1_test_prog = os.path.join(program_dir, 'Docx1_Test.py')
    prog_file = os.path.join(program_dir, 'imageExtraction.py')

    filesToRemove_upload = [os.path.join(upload_dir,f) for f in os.listdir(upload_dir)]
    # media2_path = "/home/kushal/Desktop/MTP_project/Django_MTP/mysite/media2"
    filesToRemove_csv_dir = [os.path.join(csv_dir,f) for f in os.listdir(csv_dir)]
    for f in filesToRemove_csv_dir:
        os.remove(f)
    context = {}
#   if request.method == 'GET':
    uploaded_file = request.FILES['document']
    fs = FileSystemStorage()
    name = fs.save(uploaded_file.name, uploaded_file)
    print(" \t Upload file name:{},  upload file sie :{}".format(uploaded_file.name, uploaded_file.size ))
    exec(open(docx1_test_prog).read())
    exec(open(prog_file).read())
    prog_file = os.path.join(program_dir, 'imageExtraction.py')
    exec(open(prog_file).read())
    prog_file = os.path.join(program_dir, 'imageExtraction.py')
    exec(open(prog_file).read())
    prog_file = os.path.join(program_dir, 'sectionSection.py')
    exec(open(prog_file).read())
    prog_file = os.path.join(program_dir, 'sectionTable.py')
    exec(open(prog_file).read())
    prog_file = os.path.join(program_dir, 'tableExtraction.py')
    exec(open(prog_file).read())
    prog_file = os.path.join(program_dir, 'sectionImage.py')
    exec(open(prog_file).read())
    prog_file = os.path.join(program_dir, 'sectionExtraction.py')
    exec(open(prog_file).read())
    # d = '/home/kushal/Desktop/MTP_project/Django_code/mysite/media'

    for f in filesToRemove_upload:
        print(f)
        os.remove(f)
    file_name = os.path.join(csv_dir,"Image_extraction.csv")
    df=pd.read_csv(file_name,error_bad_lines=False)
    records =  df.values.tolist()
    num = 4
    return render(request, "result.html", {'result': context,'name':name, 'columns': df.columns, 'rows': records, 'df':df,'num' : num})


def show1(request):
    csv_file_name  = os.path.join(csv_dir, "Image_extraction.csv")
    df=pd.read_csv(csv_file_name, error_bad_lines=False)
    records =  df.values.tolist()
    return render(request, 'result2.html', {'columns': df.columns, 'rows': records, 'df':df})

def show2(request):
    csv_file_name  = os.path.join(csv_dir, "Section.csv")
    df=pd.read_csv(csv_file_name, error_bad_lines=False)
    #df=pd.read_csv('/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Section.csv',error_bad_lines=False)
    records =  df.values.tolist()
    return render(request, 'result2.html', {'columns': df.columns, 'rows': records, 'df':df})

def show3(request):
    csv_file_name  = os.path.join(csv_dir, "Table_Extraction.csv")
    df=pd.read_csv(csv_file_name, error_bad_lines=False)
    #df=pd.read_csv('/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Table_Extraction.csv',error_bad_lines=False)
    records =  df.values.tolist()
    return render(request, 'result2.html', {'columns': df.columns, 'rows': records, 'df':df})

def show4(request):
    csv_file_name  = os.path.join(csv_dir, "Section_Table.csv")
    df=pd.read_csv(csv_file_name, error_bad_lines=False)
#    df=pd.read_csv('/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Section_Table.csv',error_bad_lines=False)
    records =  df.values.tolist()
    return render(request, 'result2.html', {'columns': df.columns, 'rows': records, 'df':df})

def show5(request):
    csv_file_name  = os.path.join(csv_dir, "Section_Image.csv")
    df=pd.read_csv(csv_file_name, error_bad_lines=False)
#    df=pd.read_csv('/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Section_Image.csv',error_bad_lines=False)
    records =  df.values.tolist()
    return render(request, 'result2.html', {'columns': df.columns, 'rows': records, 'df':df})

def show6(request):
    csv_file_name  = os.path.join(csv_dir, "Section_Section.csv")
    df=pd.read_csv(csv_file_name, error_bad_lines=False)
    df=pd.read_csv('/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Section_Section.csv',error_bad_lines=False)
    records =  df.values.tolist()
    return render(request, 'result2.html', {'columns': df.columns, 'rows': records, 'df':df})

def show7(request):
    exec(open("Section_Image_Count.py").read())
    df=pd.read_csv('/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Section_Image.csv',error_bad_lines=False)
    records =  df.values.tolist()
    return render(request, 'result2.html', {'columns': df.columns, 'rows': records, 'df':df})
    exec(open("test.py").read())

def show1_docx2(request):
    df=pd.read_csv('/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Image_Extraction.csv',error_bad_lines=False)
    records =  df.values.tolist()
    return render(request, 'result2.html', {'columns': df.columns, 'rows': records, 'df':df})

def show2_docx2(request):
    df=pd.read_csv('/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Section_Extraction.csv',error_bad_lines=False)
    records =  df.values.tolist()
    return render(request, 'result2.html', {'columns': df.columns, 'rows': records, 'df':df})

def show3_docx2(request):
    df=pd.read_csv('/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/table_Extraction.csv',error_bad_lines=False)
    records =  df.values.tolist()
    return render(request, 'result2.html', {'columns': df.columns, 'rows': records, 'df':df})

def show4_docx2(request):
    df=pd.read_csv('/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Section_Table.csv',error_bad_lines=False)
    records =  df.values.tolist()
    return render(request, 'result2.html', {'columns': df.columns, 'rows': records, 'df':df})

def show5_docx2(request):
    df=pd.read_csv('/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/References.csv',error_bad_lines=False)
    records =  df.values.tolist()
    return render(request, 'result2.html', {'columns': df.columns, 'rows': records, 'df':df})

def show6_docx2(request):
    df=pd.read_csv('/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Section_Section.csv',error_bad_lines=False)
    records =  df.values.tolist()
    return render(request, 'result2.html', {'columns': df.columns, 'rows': records, 'df':df})

def show7_docx2(request):
    exec(open("test.py").read())
    df=pd.read_csv('/home/kushal/Desktop/MTP_project/Django_code/mysite/media2/Section_Image.csv')
    records =  df.values.tolist()
    return render(request, 'result2.html', {'columns': df.columns, 'rows': records, 'df':df})
    exec(open("test.py").read())


def show1_latex(request):
    df=pd.read_csv('/home/kushal/Desktop/MTP_project/Django_code/mysite/Latex/ImageNames.csv')
    records =  df.values.tolist()
    return render(request, 'result2.html', {'columns': df.columns, 'rows': records, 'df':df})

def show2_latex(request):
    df=pd.read_csv('/home/kushal/Desktop/MTP_project/Django_code/mysite/Latex/SectionExtraction.csv')
    records =  df.values.tolist()
    return render(request, 'result2.html', {'columns': df.columns, 'rows': records, 'df':df})

def show3_latex(request):
    df=pd.read_csv('/home/kushal/Desktop/MTP_project/Django_code/mysite/Latex/References.csv')
    records =  df.values.tolist()
    return render(request, 'result2.html', {'columns': df.columns, 'rows': records, 'df':df})

def show4_latex(request):
    df=pd.read_csv('/home/kushal/Desktop/MTP_project/Django_code/mysite/Latex/Table_Section_Correlation.csv')
    records =  df.values.tolist()
    return render(request, 'result2.html', {'columns': df.columns, 'rows': records, 'df':df})

def show5_latex(request):
    df=pd.read_csv('/home/kushal/Desktop/MTP_project/Django_code/mysite/Latex/Section_Image_Correlation_sorted.csv')
    records =  df.values.tolist()
    return render(request, 'result2.html', {'columns': df.columns, 'rows': records, 'df':df})

def show6_latex(request):
    df=pd.read_csv('/home/kushal/Desktop/MTP_project/Django_code/mysite/Latex/Section_Section_Correlation_sorted.csv')
    records =  df.values.tolist()
    return render(request, 'result2.html', {'columns': df.columns, 'rows': records, 'df':df})

def show7_latex(request):
    exec(open("test.py").read())
    df=pd.read_csv('Section_Image.csv')
    records =  df.values.tolist()
    return render(request, 'result2.html', {'columns': df.columns, 'rows': records, 'df':df})
    exec(open("test.py").read())


def docx2(request):
    d = '/home/kushal/Desktop/MTP_project/Django_code/mysite/media2'
    filesToRemove = [os.path.join(d,f) for f in os.listdir(d)]
    for f in filesToRemove:
        os.remove(f)
    context = {}
#   if request.method == 'GET':
    uploaded_file = request.FILES['document']
    print(uploaded_file.name)
    print(uploaded_file.size)
    print("gg")
    fs = FileSystemStorage()
    name = fs.save(uploaded_file.name, uploaded_file)
    exec(open("Docx2_Test.py").read())
    exec(open("Docx2/Image_Extraction.py").read())
    exec(open("Docx2/Table_Extraction.py").read())
    exec(open("Docx2/Section_Extraction.py").read())
    exec(open("Docx2/Section_Section.py").read())
    exec(open("Docx2/Section_Table.py").read())
    exec(open("Docx2/References.py").read())
    res1=""
    d = '/home/kushal/Desktop/MTP_project/Django_code/mysite/media'
    filesToRemove = [os.path.join(d,f) for f in os.listdir(d)]
    for f in filesToRemove:
        os.remove(f)
    return render(request, "result_docx2.html", {'result': res1})

def Latex(request):
    exec(open("Latex/Bibfile.py").read())
    exec(open("Latex/Image_Extraction.py").read())
    exec(open("Latex/References.py").read())
    exec(open("Latex/Section_Extraction.py").read())
    exec(open("Latex/Section_Section.py").read())
    exec(open("Latex/Table_Extraction.py").read())
    res1=""
    return render(request, "result_latex.html", {'result': res1})
