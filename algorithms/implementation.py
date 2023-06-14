# -------------------------------------------------------------------------------------------------------------------
# 1. Grading Students
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
    for index in range(len(grades)):
        if grades[index] >= 38 and grades[index] % 5 > 2:
            grades[index] += 5 - grades[index] % 5
    return grades
            

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

# -------------------------------------------------------------------------------------------------------------------
# 2. Print all prime factors of a given number
# Python program to print prime factors
 
import math
 
# A function to print all prime factors of
# a given number n
def primeFactors(n):
     
    # Print the number of two's that divide n
    while n % 2 == 0:
        print 2,
        n = n / 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
         
        # while i divides n , print i and divide n
        while n % i== 0:
            print i,
            n = n / i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print n
         
# Driver Program to test above function
 
n = 315
primeFactors(n)
 
# This code is contributed by Harshit Agrawal
# Time Complexity : O(sqrt(n)) 
# Auxiliary Space : O(1)

# -------------------------------------------------------------------------------------------------------------------
# 3. Find all factors of a Natural Number in sorted order
# A O(sqrt(n)) java program that prints
# all divisors in sorted order
import math
 
# Method to print the divisors
 
 
def printDivisors(n):
    list = []
 
    # List to store half of the divisors
    for i in range(1, int(math.sqrt(n) + 1)):
 
        if (n % i == 0):
 
            # Check if divisors are equal
            if (n / i == i):
                print(i, end=" ")
            else:
                # Otherwise print both
                print(i, end=" ")
                list.append(int(n / i))
 
    # The list will be printed in reverse
    for i in list[::-1]:
        print(i, end=" ")
 
 
# Driver method
print("The divisors of 100 are: ")
printDivisors(100)
 
# This code is contributed by Gitanjali
# Time Complexity : O(sqrt(n)) 
# Auxiliary Space : O(sqrt(n))


# -------------------------------------------------------------------------------------------------------------------
# 4. Between two sets
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def checkValidFactor(a, b, factor):
    isFactor = True
    for bNum in b:
        if bNum % factor != 0:
            isFactor = False
            break
    if isFactor:
        for aNum in a:
            if factor % aNum != 0:
                isFactor = False
                break
    return isFactor

def getTotalX(a, b):
    # Write your code here
    
    result = 0
    minB = min(b)
    for factor in range (1, int(math.sqrt(minB)) + 1):
        if checkValidFactor(a, b, factor):
            result += 1
        if factor != round(minB / factor):
            if checkValidFactor(a, b, round(minB / factor)):
                result += 1
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
