# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 11:40:33 2019

@author: Lenovo
"""

from matplotlib import pyplot as plt

girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.xlabel("Grades Range",fontsize = 15)
#y label
plt.ylabel("Grades",fontsize = 15)
plt.title("Survey girls & boys grades ")
plt.axis([10,100,30,100])
plt.scatter(grades_range, girls_grades, marker='.', color='black',label="marker='{0}'".format('.') ); 
plt.legend()

plt.scatter(grades_range, boys_grades, marker='+', color='blue',label="marker='{0}'".format('.') ); 
plt.legend()

plt.show()

