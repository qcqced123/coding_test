def solution():
    arr = input().rstrip()
    if arr[0] == "0":
        print(0)
        return

    n = len(arr)
    dp = [0] * n
    dp[0] = 1

    if n > 1:
        if arr[1] == "0":
            if int(arr[0:2]) > 26:
                print(0)
                return
            dp[1] = 1
        else:
            dp[1] = 2 if int(arr[0:2]) <= 26 else 1

    for i in range(2, n):
        cnt = int(arr[i-1:i+1])
        if arr[i] == "0":
            if cnt > 26 or arr[i-1] == "0":
                print(0)
                return
            dp[i] = dp[i - 2] % 1000000

        else:
            if arr[i-1] != "0" and cnt <= 26:
                dp[i] = (dp[i-1] + dp[i-2]) % 1000000
            else:
                dp[i] = dp[i-1] % 1000000

    print(dp[-1] % 1000000)


if __name__ == "__main__":
    solution()
