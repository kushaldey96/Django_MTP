import csv
dict1 = {}
x1 = ""
x2 = "5. figure 1"
# print(x1)
with open('Section_Image_Count.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        x1 = row[0]
        # print(x)
        if x1 == x2:
		x = x1
		y = row[1]
		
