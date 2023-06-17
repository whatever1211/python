# -------------------------------------------------------------------------------------------------------------------
# 1. Candies
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def candies(n, arr):
    # Write your code here
    leftArr = [1] * n
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            leftArr[i] = leftArr[i-1] + 1
    rightArr = [1] * n
    for i in range(n-2, -1, -1):
        if arr[i] > arr[i+1]:
            rightArr[i] = rightArr[i+1] + 1
    finalArr = [1] * n
    for i in range(n):
        finalArr[i] = max(leftArr[i], rightArr[i])
    print(leftArr)
    print(rightArr)
    print(finalArr)
    return sum(finalArr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

# -------------------------------------------------------------------------------------------------------------------
# 2. Team Formation
import math
import heapq

# Enter your code here. Read input from STDIN. Print output to STDOUT

def solve(n, arr):
    if n == 0:
        return 0
    
    arr.sort()
    
    teams = {}
    
    for i in range(n):
        if arr[i]-1 in teams:            
            temp = heapq.heappop(teams[arr[i]-1])
            if len(teams[arr[i]-1]) == 0:
                del teams[arr[i]-1]
            if arr[i] not in teams:
                teams[arr[i]] = []
                heapq.heapify(teams[arr[i]])
            heapq.heappush(teams[arr[i]], temp + 1)
        else:
            if arr[i] not in teams:
                teams[arr[i]] = []
                heapq.heapify(teams[arr[i]])
            heapq.heappush(teams[arr[i]], 1)
                    
    result = math.inf
    for team in teams.values():
        if result > min(team):
            result = min(team)    
    return result

if __name__ == "__main__":
    t = int(input().strip())
    
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        
        n = arr.pop(0) # Remove n
        
        arr.sort()
        
        result = solve(n, arr)
        
        print(result)
