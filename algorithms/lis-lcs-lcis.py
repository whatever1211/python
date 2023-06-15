# LIS
def LIS(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print(LIS(arr))

# LCIS
def LCIS(arr1, arr2):
    l1 = len(arr1)
    l2 = len(arr2)
    dp = [0] * l2
    for i in range(l1):
        current = 0
        for j in range(l2):
            if arr1[i] == arr2[j]:
                dp[j] = max(current + 1, dp[j])
            if arr1[i] > arr2[j]:
                current = max(current, dp[j])
    result = max(dp)
    return result
a1 = [2, 4, 9, 1]
a2 = [2, 5, 8, 4, 9, 0, 1]
print("Length of LCIS is: ", LCIS(a1, a2))

# LCS
def lcs_algo(S1, S2, m, n):
    L = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif S1[i-1] == S2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    index = L[m][n]

    lcs_algo = [""] * (index+1)
    lcs_algo[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:
        if S1[i-1] == S2[j-1]:
            lcs_algo[index-1] = S1[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1

    print("S1 : " + S1 + "\nS2 : " + S2)
    print("LCS: " + "".join(lcs_algo))


S1 = "ACADB"
S2 = "CBDA"
m = len(S1)
n = len(S2)
lcs_algo(S1, S2, m, n)
