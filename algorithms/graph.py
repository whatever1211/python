# -------------------------------------------------------------------------------------------------------------------
# Journey to the Moon
#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(1000 * 1000)

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#

def dfs(start, astronaut, check, nation, curNation):
    if check[start]:
        return
    check[start] = True
    nation[start] = curNation
    for i in astronaut[start]:
        if not check[i]:
            dfs(i, astronaut, check, nation, curNation)

def journeyToMoon(n, astronaut):
    # Write your code here
    check = [False] * n
    nation = [-1] * n
    curNation = 0
    
    for i in range(n):
        if not check[i]:
            curNation += 1
            dfs(i, astronaut, check, nation, curNation)
    
    print(check)
    print(nation)
    print(curNation)
            
    countNationAstro = [0] * curNation
    for i in range(n):
        countNationAstro[nation[i] - 1] += 1        
            
    sumCurNation = sum(countNationAstro)
    result = 0
    for i in range(curNation - 1):
        result += countNationAstro[i] * (sumCurNation - countNationAstro[i])
        sumCurNation -= countNationAstro[i]        
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])
    
    astronaut = [{} for _ in range(n)]

    for _ in range(p):
        nodeX, nodeY = list(map(int, input().rstrip().split()))
        if nodeY not in astronaut[nodeX]: astronaut[nodeX][nodeY] = True
        if nodeX not in astronaut[nodeY]: astronaut[nodeY][nodeX] = True
    
    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()

# -------------------------------------------------------------------------------------------------------------------
# Roads and Libraries
#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(1000 * 1000)

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def dfs(start, cities, check, city, curCity):
    if check[start]:
        return
    check[start] = True
    city[start] = curCity
    for i in cities[start]:
        if not check[i]:
            dfs(i, cities, check, city, curCity)

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    
    if c_lib <= c_road:
        return c_lib * n
    
    check = [False] * n
    city = [-1] * n    
    curCity = 0
    
    for i in range(n):
        if not check[i]:
            curCity += 1
            dfs(i, cities, check, city, curCity)
            
    countCityNode = [0] * curCity
    for i in range(n):
        countCityNode[city[i] - 1] += 1
        
    print(check)
    print(city)
    print(curCity)    
    print(countCityNode)
    
    result = 0
    for i in range(curCity):
        result += c_road * (countCityNode[i] - 1)
    
    result += c_lib * curCity
        
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = [{} for _ in range(n)]

        for _ in range(m):
            nodeX, nodeY = list(map(int, input().rstrip().split()))
            if (nodeY - 1) not in cities[nodeX - 1]: cities[nodeX - 1][nodeY - 1] = True            
            if (nodeX - 1) not in cities[nodeY - 1]: cities[nodeY - 1][nodeX - 1] = True            

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
