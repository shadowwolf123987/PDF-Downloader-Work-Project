
import requests
import time
import csv
import googlesearch
from googlesearch import search

rowsTemp=[]
rows=[]
links=[]
rows2 = []
hrefs = []
pdfsRaw = []
pdfs = []
pdfsFilt = []



with open("Data.csv", newline="") as csvfile:
    reader=csv.reader(csvfile,quotechar="|")
    for row in reader:
        rowsTemp.append(row)

x=0
while x != len(rowsTemp):
    if x%2==0:
        rows.append(rowsTemp[x])
        x+=1
    else:
        x+=1


x=0
while x != len(rows):
    rowsSplit = str(rows[x]).split("'")
    rows2.append(str(rowsSplit[1]))
    x+=1

x=0
while x != len(rows):
    query = str('site:"notifierfiresecurity.com filetype:pdf ' + rows2[x])
    print(query)
    for y in search(query,tld="co.in", num=1):
        links.append(y)
        print(y)
        time.sleep(30)
    x+=1
