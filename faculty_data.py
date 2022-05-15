
import requests
from bs4 import BeautifulSoup
from tabula.io import read_pdf
from tabulate import tabulate
import pandas as pd
import numpy as np


# to get research interests as well as brief research profile

link= 'https://www.nitj.ac.in/index.php/nitj_cinfo/Faculty/212'
r= requests.get(link)
soup=BeautifulSoup(r.content,'html.parser')
interests=soup.find('div',class_='col-md-12 mix Research-Profile')
data=interests.find_all('td')
title=['rinterests','brief_profile']
j=0
rdata={}
for i in range(1,len(data)+1):
  if i%3==0:
    rdata[title[j]]=data[i-1].text.strip()
    j+=1

for key,val in rdata.items():
  print(key+" "+val)




# to scrape personal details like name designation qualification etc
# NEED TO WORK ON THIS PART OF CODE ##
# PRINTING FIRST TWO DETAILS ONLY AS OF NOW #


details=['name','designation','department','qualification','address','phone','id','fax']
pdata={}
personal=soup.find('div','menu-content')
tabledata=personal.find_all('table')
data2=tabledata[1].find_all('td')
j=0
for i in range(1,len(data2)+1):
  if i%3==0:
    pdata[details[j]]=data2[i-1].text.strip()
    j+=1
for key,value in pdata.items():
  print(key+" "+value)





tables=read_pdf("https://www.nitj.ac.in/Faculty/profile-pdf.php?id=212",pages="all",multiple_tables=True,lattice=True)
# tables is a list of all tables present in PDF of profile generated from actual website
# all tables can be used using indexing tables[0],tables[1] and so on
print(tables[0])
print(tables[1])

# dumping the table in csv format using '$' as separator because ',' is present in text
## CSV isn't the only option, you can also use to_excel(), to_html(), to_json() and to_sqlite() methods  ##
tables[0].to_csv('sample.csv')




