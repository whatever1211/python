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

# -------------------------------------------------------------------------------------------------------------------
# 3. Cloudy Day
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPeople' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY p
#  2. LONG_INTEGER_ARRAY x
#  3. LONG_INTEGER_ARRAY y
#  4. LONG_INTEGER_ARRAY r
#

def maximumPeople(p, x, y, r):
    cities = [[i[0], i[1]] for i in zip(x, p)]  # cities or towns
    cities = sorted(cities, key=lambda x: (x[0]))

    clouds = [[max(1, i[0]-i[1]), i[0]+i[1]] for idx, i in enumerate(zip(y, r))]
    clouds = sorted(clouds, key=lambda x: (x[0]))

    len_cloud = len(clouds)
    idx = 0
    start = 0
    sum_sunny = 0
    cloud_city = [0 for _ in range(len_cloud)]
    for j in cities:
        count = []
        check = True
        idx = start

        while idx < len_cloud:
            i = clouds[idx]
            if check and i[1] < j[0]:
                start = idx+1
                idx += 1
                continue

            if i[1] >= j[0]:
                check = False

            if i[0] <= j[0] and j[0] <= i[1]:
                count.append(idx)

            if len(count) > 1:
                break

            if i[0] > j[0]:
                break

            idx += 1

        if len(count) == 0:
            sum_sunny += j[1]
        if len(count) == 1:
            cloud_city[count[0]] += j[1]


    sum_cloud = max(cloud_city)
    # print(cities, selected_clouds)
    # print(sum_sunny, sum_cloud)
    return sum_sunny + sum_cloud

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    fptr.write(str(result) + '\n')

    fptr.close()
