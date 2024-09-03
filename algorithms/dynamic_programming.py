# -------------------------------------------------------------------------------------------------------------------
# 1. Two Robots
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoRobots' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER m
#  2. 2D_INTEGER_ARRAY queries
#

def twoRobots(m, queries):
    # Write your code here
    prev_bot = queries[0][0]
    mintotal = 0
    containers = [0]*(m+1)

    for a, b in queries:
        distance = abs(a-b)
        traveled = abs(prev_bot-a)+distance

        minimums = min(abs(k-a)+v for k, v in enumerate(containers))
        minimums = min(mintotal, minimums)
        mintotal += traveled

        containers[:] = [v+traveled for v in containers]
        containers[prev_bot] = minimums+distance
        prev_bot = b

    return min(containers)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for _ in range(t):

        first_multiple_input = input().rstrip().split()

        m = int(first_multiple_input[0])

        n = int(first_multiple_input[1])

        queries = []

        for _ in range(n):
            queries.append(list(map(int, input().rstrip().split())))

        result = twoRobots(m, queries)

        fptr.write(str(result) + '\n')

    fptr.close()
