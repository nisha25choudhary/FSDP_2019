#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    fi = []
    for i in grades:
        if i < 38:
            fi.append(i)
        elif i % 5 != 0:
                nextm = (i//5+1)*5
                final  =  nextm - i
                if final < 3:
                    fi.append(nextm)
                else:
                    fi.append(i)
        else:
            fi.append(i)
    return fi
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()




 
