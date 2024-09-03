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
    cities = []
    for i in range(len(p)):
        cities.append([x[i], p[i]])
    
    cloud_start = []
    cloud_end = []
    clouds = set()
    
    for i in range(len(y)):
        cloud_start.append([y[i] - r[i], i])
        cloud_end.append([y[i] + r[i], i])
    
    cities = sorted(cities)
    cloud_start = sorted(cloud_start)
    cloud_end = sorted(cloud_end)
    
    cloudy = {}
    sunny = 0
    
    cloud_start_i = 0
    cloud_end_i = 0
    
    for city_i in range(len(cities)):
        city_x = cities[city_i][0]
        
        while cloud_start_i < len(cloud_start) and cloud_start[cloud_start_i][0] <= city_x:
            clouds.add(cloud_start[cloud_start_i][1])
            cloud_start_i += 1
        
        while cloud_end_i < len(cloud_end) and cloud_end[cloud_end_i][0] < city_x:
            clouds.remove(cloud_end[cloud_end_i][1])
            cloud_end_i += 1
            
        if len(clouds) == 1:
            cloud_start_x = list(clouds)[0]
            if cloud_start_x in cloudy:
                cloudy[cloud_start_x] += cities[city_i][1]
            else:
                cloudy[cloud_start_x] = cities[city_i][1]
        elif len(clouds) == 0:
            sunny += cities[city_i][1]
    
    return max(cloudy.values(), default=0) + sunny

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
