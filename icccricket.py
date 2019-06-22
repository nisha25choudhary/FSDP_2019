# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:24:12 2019

@author: Lenovo
"""

from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi").text

#print(source)

soup = BeautifulSoup(source,"lxml")
#print(soup)
#print (soup.prettify())

right_table=soup.find('table', class_='table')

#print (right_table.prettify())


team = []
weight = []
point = []
rat = []



for row in right_table.findAll('tr'):
    cells = row.findAll('td') 
   
    if len(cells) == 5:
         #skip the sequence number column
        team.append(cells[1].text.strip())
        weight.append(cells[2].text.strip())
        point.append(cells[3].text.strip())
        rat.append(cells[4].text.strip())
 


from collections import OrderedDict

col_name = ["Team","Weighted Matches","Points","Rating"]
col_data = OrderedDict(zip(col_name,[team,weight,point,rat]))


import pandas as pd
df = pd.DataFrame(col_data) 
print(df)
df.to_csv("rating.csv",index=False)




# Solution for the Code Challenge of ICC Ranking 
from bs4 import BeautifulSoup
import pandas as pd
import requests

lnk = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
pg = requests.get(lnk).text
sp = BeautifulSoup(pg,"lxml")

my_tab = sp.find('table',class_="table")


A=[]
B=[]
C=[]
D=[]
E=[]


for bdy in my_tab.find_all("tbody"):
    for row in bdy.find_all("tr"):
        cel = row.find_all('td')
        A.append(cel[0].text.strip())
        B.append(cel[1].text.strip())
        C.append(cel[2].text.strip())
        D.append(cel[3].text.strip())
        E.append(cel[4].text.strip())

df = pd.DataFrame()
df["Position"]=A
df["Team"]=B
df["Matches"]=C
df["Points"]=D
df["Rating"]=E
  
df.to_csv("data/ODI_Ranking_2017.csv", index=False)


