import csv
import os
dict1 = {}
x = ""
CUR_BASE_DIR = os.path.join("/home/kushal/Desktop/MTP_project/Django_MTP" ,"mysite", "media2")
guestFileName = os.path.join(CUR_BASE_DIR, 'Section_Section.csv')
with open(guestFileName) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        x = row[0] + " " + row[1]
        if x in dict1.keys():
            dict1[x] = dict1[x]+1
        else:
            dict1[x] = 1

print("Gg")
CUR_BASE_DIR = os.path.join("/home/kushal/Desktop/MTP_project/Django_MTP" ,"mysite", "media2")
guestFileName = os.path.join(CUR_BASE_DIR, 'Section_Image_Count.csv')
with open(guestFileName, 'w') as f:
    for key in dict1.keys():
        f.write("%s,%s\n" % (key, dict1[key]))
        print(key, dict1[key])

import pandas as pd
CUR_BASE_DIR = os.path.join("/home/kushal/Desktop/MTP_project/Django_MTP" ,"mysite", "media2")
guestFileName = os.path.join(CUR_BASE_DIR, 'Section_Image_Count.csv')
dataset = pd.read_csv(guestFileName)
x1 = dataset.iloc[:, 0].values
y1 = dataset.iloc[:, 1].values

print(x1,y1)

from bokeh.io import show, output_file
from bokeh.plotting import figure
guestFileName = os.path.join(CUR_BASE_DIR, 'bars.html')
output_file(guestFileName)

fruits = x1
counts = y1

p = figure(x_range=fruits, plot_height=250, title="Fruit Counts",
           toolbar_location=None, tools="")

p.vbar(x=fruits, top=counts, width=0.9)

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)
