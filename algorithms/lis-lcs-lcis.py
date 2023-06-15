# LIS
def LIS(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print(LIS(arr))

