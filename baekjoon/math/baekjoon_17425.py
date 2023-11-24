import sys
"""
[풀이]
1) 약수를 뒤집어 생각하면 배수
=> 생각한 것도 맞고, 코드도 거기서 거기인듯 한데 뭐가 도대체 차이가 나는건지 모르겠다.
"""


arr = [1]*1000001  # 입력 최대 길이: 100만, 한번이라도 루프를 줄여주기 위해 1을 더하고 시작
dp = [0]*1000001
T = int(sys.stdin.readline())
for i in range(2, 1000001):  # 1은 더하고 시작 했으니까, 2부터 시작
    j = 1
    while i*j <= 1000000:
        arr[i*j] += i  # 현재 대상 숫자를 배수에 전부 더하기
        j += 1
    # arr[i] += arr[i-1]
for i in range(1, 1000001):
    dp[i] = dp[i-1] + arr[i]  # 배열 하나 쓰는 것보다 두개 쓰는게 더 빨랐음

for _ in range(T):
    sys.stdout.write(f"{(dp[int(sys.stdin.readline())])}\n")

