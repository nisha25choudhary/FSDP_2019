# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 13:00:18 2019

@author: Lenovo
"""

import mysql.connector 

from pandas import DataFrame
from selenium import webdriver

bid = "https://bidplus.gem.gov.in/bidlists"

driver = webdriver.Chrome("C:\\Users\\Lenovo\\Downloads\\python\\chromedriver.exe")

driver.get(bid)

conn = mysql.connector.connect(user='nisha123', password='nisha234',host='db4free.net', database = 'bidplus')
c = conn.cursor()

c.execute("DROP TABLE bdip")


c.execute ("""CREATE TABLE bdip(
          bidno TEXT,
          item  TEXT,
          qunt TEXT,
          dprt TEXT,
          sd TEXT,
          ed TEXT
          )""")


i = 1
for i in range(1,11):
    bidno1 = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a')
    b = bidno1.text
    item1 =  driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span')
    it = item1.text
    qunt1 =  driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span')
    q = qunt1.text
    dprt1 =  driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]')
    d = dprt1.text
    sd1 =  driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span')
    s = sd1.text
    ed1 =  driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span')
    e = ed1.text
    c.execute("INSERT INTO bdip VALUES "+ "('{}','{}','{}','{}','{}','{}')".format(b,it,int(q),d,s,e))
    
    
c.execute("SELECT * FROM bdip")

print ( c.fetchall() )

 
conn.commit()


c.execute("SELECT * FROM bdip")

df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["BDI NO","Item's","Quntity","Departement Name","Start Date","End Date"]

conn.close()
 
 