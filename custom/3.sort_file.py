import math
import os
import random
import re
import sys

def clear_pos(pos, arr, need_clear_arr, cleared_arr):
    height = arr[pos]
    left = pos
    right = pos

    while left >= 0:
        if (need_clear_arr[left]):
            cleared_arr[left] = True
        elif (arr[left] >= height):
            break
        left -= 1

    while right < len(arr):
        if (need_clear_arr[right]):
            cleared_arr[right] = True
        elif (arr[right] >= height):
            break
        right += 1

if __name__ == "__main__":
    # fptr = open("input.txt", "r")

    n = int(input().strip())

    arr = []

    need_clear_arr = [False] * n
    cleared_arr = [False] * n

    need_clear_arr_only = []

    for i in range(n):
        clear, value = list(input().rstrip().split())
        value = int(value)
        arr.append(value)
        if clear == "y":
            need_clear_arr[i] = True
            need_clear_arr_only.append((value, i))
        else:
            need_clear_arr[i] = False

    # fptr.close()

    need_clear_arr_only.sort()

    # print(arr)
    # print(need_clear_arr_only)

    result = 0

    for i in range(len(need_clear_arr_only)):
        pos = need_clear_arr_only[i][1]
        if not cleared_arr[pos]:
            clear_pos(pos, arr, need_clear_arr, cleared_arr)
            result += 1

    print(result)