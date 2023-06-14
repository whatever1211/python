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

# -------------------------------------------------------------------------------------------------------------------
# 5. Queens attack 2
#!/bin/python3

n, k = map(int, input().split())
rQueen, cQueen = map(int, input().split())
obstacles = set()
for _ in range(k):
    rObs, cObs = map(int, input().split())
    obstacles.add((rObs, cObs))
ans = 0
# left
r, c = rQueen, cQueen - 1
while c > 0:
    if (r, c) in obstacles:
        break
    ans, c = ans + 1, c - 1
# right
r, c = rQueen, cQueen + 1
while c <= n:
    if (r, c) in obstacles:
        break
    ans, c = ans + 1, c + 1
# up
r, c = rQueen + 1, cQueen
while r <= n:
    if (r, c) in obstacles:
        break
    ans, r = ans + 1, r + 1
# down
r, c = rQueen - 1, cQueen
while r > 0:
    if (r, c) in obstacles:
        break
    ans, r = ans + 1, r - 1
# upper right
r, c = rQueen + 1, cQueen + 1
while r <= n and c <= n:
    if (r, c) in obstacles:
        break
    ans, r, c = ans + 1, r + 1, c + 1
# upper left
r, c = rQueen + 1, cQueen - 1
while r <= n and c > 0:
    if (r, c) in obstacles:
        break
    ans, r, c = ans + 1, r + 1, c - 1
# lower left
r, c = rQueen - 1, cQueen - 1
while r > 0 and c > 0:
    if (r, c) in obstacles:
        break
    ans, r, c = ans + 1, r - 1, c - 1
# lower right
r, c = rQueen - 1, cQueen + 1
while r > 0 and c <= n:
    if (r, c) in obstacles:
        break
    ans, r, c = ans + 1, r - 1, c + 1
print(ans)

# -------------------------------------------------------------------------------------------------------------------
# 6. Hash Table 
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
 
    def create_buckets(self):
        return {}
 
    def set_val(self, key, val):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table.get(hashed_key)
        if bucket:
            found_key = False
            for index, record in enumerate(bucket):
                record_key, record_val = record
                if record_key == key:
                    found_key = True
                    break
            if found_key:
                bucket[index] = (key, val)
            else:
                bucket.append((key, val))
        else:
            self.hash_table[hashed_key] = []
            self.hash_table[hashed_key].append((key, val))
 
    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table.get(hashed_key)
        if bucket:
            found_key = False
            for index, record in enumerate(bucket):
                record_key, record_val = record
                if record_key == key:
                    found_key = True
                    break
            if found_key:
                return record_val
            else:
                return None
        else:
            return None
 
    def delete_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table.get(hashed_key)
        if bucket:
            found_key = False
            for index, record in enumerate(bucket):
                record_key, record_val = record
                if record_key == key:
                    found_key = True
                    break
            if found_key:
                bucket.pop(index)
    def __str__(self):
        return "\n".join(str(item) + " " + str(self.hash_table[item]) for item in self.hash_table)

def gridSearch(R, C, G, r, c, P):
    # Write your code here
    gridHashTable = HashTable(pow(10, 9) + 7)
    for i in range(R):
        for j in range(C - c + 1):
            tempStr = G[i][j:j+c]
            gridHashTable.set_val(tempStr, True)
    for i in range(r):
        if not gridHashTable.get_val(P[i]):
            return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(R, C, G, r, c, P)

        fptr.write(result + '\n')

    fptr.close()
