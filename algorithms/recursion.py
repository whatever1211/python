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

# -------------------------------------------------------------------------------------------------------------------
# 2. Password Cracker
#!/bin/python3

import math
import os
import random
import re
import sys

sys.setrecursionlimit(1000 * 1000) # Default 1000

#
# Complete the 'passwordCracker' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY passwords
#  2. STRING loginAttempt
#

def passwordCracker(passwords, loginAttempt, failArr, loginAttempCurrentLength):
    # Write your code here
    if failArr[loginAttempCurrentLength]:
        return []
    result = []
    for passwd in passwords:
        if passwd == loginAttempt[:len(passwd)] and len(passwd) == len(loginAttempt[:len(passwd)]):
            if len(passwd) == len(loginAttempt):
                result.append(passwd)
                break
            else:
                passwdArr = passwordCracker(passwords, loginAttempt[len(passwd):], failArr, loginAttempCurrentLength + len(passwd))
                if passwdArr:
                    passwdArr.append(passwd)
                    result = passwdArr
                    break
    if not result:
        failArr[loginAttempCurrentLength] = True
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        passwords = input().rstrip().split()

        loginAttempt = input()
        
        failArr = [False for _ in range(len(loginAttempt) + 1)]

        result = passwordCracker(passwords, loginAttempt, failArr, 0)
        
        if result:
            result.reverse()
            result = " ".join(result)
        else:
            result = "WRONG PASSWORD"

        fptr.write(result + '\n')

    fptr.close()

    fptr.close()
