# -------------------------------------------------------------------------------------------------------------------
# 1. The Power Sum
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#

def powerSum(X, N, B):
    # Write your code here
    result = 0
    for i in range(B + 1, X):
        if i ** N < X:
            result += powerSum(X - i ** N, N, i)
        elif i ** N == X:
            result += 1
        else:
            break
    return result
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N, 0)

    fptr.write(str(result) + '\n')

    fptr.close()
