#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    new=s[:8]
    if s[8:10]=="PM" and s[0:2]!="12":
        new=str(int(new[0:2])+12) +new[2:10]
    if s[8:10]=="AM" and s[0:2]=="12":
        new="00" + new[2:10]
    return new
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
