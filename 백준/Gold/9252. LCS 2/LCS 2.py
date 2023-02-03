arr1 = list(input())
arr2 = list(input())


dp = [[""] * (len(arr2) + 1) for _ in range(len(arr1) + 1)]
for i in range(1, len(arr1) + 1):
    for j in range(1, len(arr2) + 1):
        if arr1[i - 1] == arr2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + arr1[i - 1]
        else:
            if len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

if len(dp[-1][-1]) == 0:
    print(0)
else:
    print(len(dp[-1][-1]))
    print(dp[-1][-1])