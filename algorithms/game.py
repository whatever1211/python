# -------------------------------------------------------------------------------------------------------------------
# 1. Game of Stones
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfStones' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def gameOfStones(n, nArr):
    # Write your code here
    if nArr[n]: return nArr[n]
    result = None
    if n == 0:
        result = "Lose"
    elif n == 1:
        result = "Lose"
    elif n == 2:
        result = "Win"
    elif n == 3:
        result = "Win"
    elif n == 4:
        result = "Win"
    elif n == 5:
        result = "Win"
    else:
        # result = "Win" if gameOfStones(n - 2, nArr) == "Lose" or gameOfStones(n - 3, nArr) == "Lose" or gameOfStones(n - 5, nArr) == "Lose" else "Lose"
        result = "Lose" if gameOfStones(n - 2, nArr) == "Win" and gameOfStones(n - 3, nArr) == "Win" and gameOfStones(n - 5, nArr) == "Win" else "Win"
    nArr[n] = result
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        
        nArr = [None] * (n + 1)

        result = "First" if gameOfStones(n, nArr) == "Win" else "Second"

        fptr.write(result + '\n')

    fptr.close()

# -------------------------------------------------------------------------------------------------------------------
# 2. Tower Breakers
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    # Write your code here
    if m == 1:
        return 2
    if n % 2 == 0:
        return 2
    return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
