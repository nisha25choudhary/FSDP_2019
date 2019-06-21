# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 20:41:21 2019

@author: Lenovo
"""



from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


fortune = "https://astrologyfutureeye.com/fortune-tellers/name-predictor"
driver = webdriver.Chrome("C:\\Users\\Lenovo\\Downloads\\python\\chromedriver.exe")
driver.get(fortune)

sleep(2)
 
user_name = driver.find_element_by_xpath('//*[@id="namepredictor"]/input[1]')
name = "mini"
user_name.send_keys(name)

sleep(2)
get_name_page = driver.find_element_by_xpath('//*[@id="sub"]')
get_name_page.click()

sleep(5)

ls = []
element  = driver.find_element_by_xpath('//*[@id="result"]')
 
ls.append(element.text)

with open('info_name.txt','w+',encoding='utf-8') as nm:
     for listitem in ls:
         nm.write(listitem)
 
    
driver.close()
'''
myfile = open('alice.txt', encoding='utf-8')     # Reading a UTF-8 file; 'r' is omitted

#ls1 = ["hello mini,\n predict name"]
with open('n.txt','w') as nn:
    for i in ls1:
        nn.write(i)
'''

element  = driver.find_Element_by_xpath('//*[@id="result"]')

element.send_keys(Keys.CONTROL + 'a')


 