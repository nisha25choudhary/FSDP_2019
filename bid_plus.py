# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 11:03:08 2019

@author: Lenovo
"""


from selenium import webdriver

bid = "https://bidplus.gem.gov.in/bidlists"

driver = webdriver.Chrome("C:\\Users\\Lenovo\\Downloads\\python\\chromedriver.exe")

driver.get(bid)


bidno = []
item = []
qunt = []
dprt = []
sd = []
ed = []
'''
bidno1 = driver.find_element_by_xpath('//*[@id="pagi_content"]/div[2]/div[1]/p[1]/a')
print(bidno1.text)

item = driver.find_element_by_xpath('//*[@id="pagi_content"]/div[2]/div[2]')
print(item.text)

dprt = driver.find_element_by_xpath('//*[@id="pagi_content"]/div[2]/div[3]')
print(dprt.text)

sd = driver.find_element_by_xpath('//*[@id="pagi_content"]/div[2]/div[4]')
print(sd.text)
'''
i = 1
for i in range(1,11):
    bidno1 = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a')
    bidno.append(bidno1.text)
    item1 =  driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span')
    item.append(item1.text)
    qunt1 =  driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span')
    qunt.append(qunt1.text)
    dprt1 =  driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]')
    dprt.append(dprt1.text)
    sd1 =  driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span')
    sd.append(sd1.text)
    ed1 =  driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span')
    ed.append(ed1.text)
'''    
print(bidno)
print(item)      
print(qunt)      
print(dprt)      
print(sd)      
print(ed)      '''


import pandas as pd
from collections import OrderedDict

col_name = ["BID NO","Item(s)","Quantity Required","Department Name And Address", "Start Date","End Date"]
col_data = OrderedDict(zip(col_name,[bidno,item,qunt,dprt,sd,ed]))
df = pd.DataFrame(col_data) 
df.to_csv("bid_plus.csv")


result = driver.find_element_by_xpath('//*[@id="pagi_content"]/div[2]/div[1]/p[1]/a')
result.click()







    
from selenium import webdriver
from time import sleep
import csv

bids=[]
itemss=[]
quantitys=[]
addresss=[]
start_date_time=[]
end_date_time=[]
start_dates=[]
start_time=[]
end_time=[]
end_dates=[]

options = webdriver.ChromeOptions()
browser = webdriver.Chrome(chrome_options=options)
url="https://bidplus.gem.gov.in/servicelists"

browser.get(url)

for i in range(1,11):
    path_bid='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[1]/p[1]/a'''
    try:
        bid_no=browser.find_element_by_xpath(path_bid)
    except Exception as e:
        print("[ERROR]: "+str(e))
        break
    bids.append(bid_no.text)
    
    path_items='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[2]/p[1]/span'''
    items=browser.find_element_by_xpath(path_items)
    itemss.append(items.text)
    
    path_quantity='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[2]/p[2]/span'''
    quantity=browser.find_element_by_xpath(path_quantity)
    quantitys.append(quantity.text)
    
    path_address='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[3]/p[2]'''
    address=browser.find_element_by_xpath(path_address)
    addresss.append(address.text)
    
    path_start_date='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[4]/p[1]/span'''
    start_date=browser.find_element_by_xpath(path_start_date)
    start_date_time.append(start_date.text)
    
    path_end_date='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[4]/p[2]/span'''
    end_date=browser.find_element_by_xpath(path_end_date)
    end_date_time.append(end_date.text)
    
    bid_no.click()
sleep(10)
browser.quit() 

for z in range(0,len(start_date_time)):
    start_dates.append(start_date_time[z][:10])
    start_time.append(start_date_time[z][10:])
    end_dates.append(end_date_time[z][:10])
    end_time.append(end_date_time[z][10:])
  



with open("bid_plus.csv","r+") as file:
    write=csv.writer(file,delimiter=",")
    write.writerow(["BID NO","Items","Quantity","Address","Start Date","Start Time","End Time","End Time"])
    for i in range(len(bids)):
        tmp_lst = [bids[i],itemss[i],quantitys[i],addresss[i],start_dates[i],start_time[i],end_dates[i],end_time[i]]
        for i in range(len(tmp_lst)):
            tmp_lst[i] = tmp_lst[i].replace("\n"," ")
        write.writerow(tmp_lst)

