# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:55:17 2019

@author: Lenovo
"""
client = pymongo.MongoClient("mongodb://nisha:<password>@cluster0-shard-00-00-y0khe.mongodb.net:27017,cluster0-shard-00-01-y0khe.mongodb.net:27017,cluster0-shard-00-02-y0khe.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
 

mongodb://nisha:<password>@cluster0-shard-00-00-y0khe.mongodb.net:27017,cluster0-shard-00-01-y0khe.mongodb.net:27017,cluster0-shard-00-02-y0khe.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority

import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb://nisha:nisha%40123@cluster0-shard-00-00-y0khe.mongodb.net:27017,cluster0-shard-00-01-y0khe.mongodb.net:27017,cluster0-shard-00-02-y0khe.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test


mydb = client.university


def add_stud(name, age, rollno, branch):
    #unique_employee = mydb.students.find_one({"id":name})
    #if unique_employee:
     #   return "Employee already exists"
    #else:
    mydb.students.insert_one(
            {
                    "name" : name,
                    "age" : age,
                    "rollno" : rollno,
                    "branch" : branch
                    })
    return "Employee added successfully"

def fetch_all_stud():
    user = mydb.students.find()
    for i in user:
        print (i)

mydb.students.drop()

add_stud('Nisha',20, 101, 'CS')
add_stud('Hanu',21, 102, 'CS')
add_stud('Meenal',20, 103, 'CSE')
add_stud('Naveen',22, 104, 'MGMT')
add_stud('Annu',20, 105, 'MGMT')
add_stud('Ugam',23, 106, 'LOW')
add_stud('Rekha',20, 107, 'LOW')
add_stud('Sanju',24, 108, 'CS')
add_stud('Dipti',22, 109, 'EE')
add_stud('Yogi',25, 110, 'EE')

fetch_all_stud()


