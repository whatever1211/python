# -------------------------------------------------------------------------------------------------------------------
# 1. Strong Password 
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    number_count = 0
    lower_case_count = 0
    upper_case_count = 0
    special_count = 0
    for char in password:
        if char in numbers: number_count += 1
        if char in lower_case: lower_case_count += 1
        if char in upper_case: upper_case_count += 1
        if char in special_characters: special_count += 1
    
    missing_char = 0
    if number_count == 0: missing_char += 1
    if lower_case_count == 0: missing_char += 1
    if upper_case_count == 0: missing_char += 1
    if special_count == 0: missing_char += 1
    
    missing_len = 6 - n
    
    return max(missing_char, missing_len)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
