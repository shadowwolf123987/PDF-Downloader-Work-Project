
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
exceptions = []


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
while x != len(rows2):
    keywords = str('site:notifierfiresystems.co.uk filetype:pdf ' + rows2[x])
    print(keywords)
    results = ddg(keywords)
    print(results)
    results = results[0]
    try:
        temp=results["href"]
    except IndexError:
        print("error")
        exceptions.append(rows2[x])
        x+=1
    print("\n")
    links.append(results["href"])
    response = requests.get(results["href"])
    if "/" in results["title"]:
        results["title"] = results["title"].replace("/"," ")
    path = "F:\\My Files\\Documents\\Oli\\Scripts\\Visual Studio\\Python\\Dad\\Shittier PDF Downloader\\Datasheets\\" + (str(results["title"])) + ".pdf"
    print(x)
    with open (path,"wb") as file:
        file.write(response.content)
    x+=1

print(exceptions)