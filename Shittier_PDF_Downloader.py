
from pathlib import Path
import requests
import time
import csv
import googlesearch
from duckduckgo_search import ddg
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
        rows.append(row)

x=0
##while x != len(rowsTemp):
  ##  if x%2==0:
    ##    rows.append(rowsTemp[x])
      ##  x+=1
   ## else:
    ##    x+=1


x=0
while x != len(rows):
    rowsSplit = str(rows[x]).split("'")
    rows2.append(str(rowsSplit[1]))
    x+=1

x=0
while x != len(rows):
    query = str('site:"notifierfiresecurity.com filetype:pdf ' + rows2[x])
    print(query)
    for y in ddg(query):
        links.append(y["href"])
        print(y["href"])
        response = requests.get(y["href"])
        path = "F:\\My Files\\Documents\\Oli\\Scripts\\Visual Studio\\Python\\Dad\\Shittier PDF Downloader\\Datasheets\\" + (str(y["title"])) + ".pdf"
        print(x)
        with open (path,"wb") as file:
            file.write(response.content)
    x+=1