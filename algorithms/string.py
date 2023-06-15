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

# -------------------------------------------------------------------------------------------------------------------
# 2. Highest Value Palindrome
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    # Write your code here
    sArr = [char for char in s]
    minimum_change_require = 0
    for i in range(math.floor(n / 2)):
        if sArr[i] != sArr[n - 1 - i]:
            minimum_change_require += 1
    if minimum_change_require > k:
        return "-1"
    i = 0
    print (i, k, minimum_change_require)
    while i < math.floor(n / 2):
        if sArr[i] == sArr[n - 1 - i]:
            if k - minimum_change_require > 1 and sArr[i] != "9":
                sArr[i] = "9"
                sArr[n - 1 - i] = "9"
                k -= 2
        else:
            if k - minimum_change_require > 0:
                minusK = 0
                if sArr[i] != "9":
                    minusK += 1
                    sArr[i] = "9"
                if sArr[n - 1 - i] != "9":
                    minusK += 1
                    sArr[n - 1 - i] = "9"
                k -= minusK
                minimum_change_require -= 1
            else:
                maxS = str(max(int(sArr[i]), int(sArr[n - 1 - i])))
                sArr[i] = maxS
                sArr[n - 1 - i] = maxS
                k -= 1
                minimum_change_require -= 1
        i += 1
    print (i, k, minimum_change_require)
    if n % 2 == 1 and sArr[i] != "9":
        if k - minimum_change_require > 0:
            sArr[i] = "9"
    return "".join(sArr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
