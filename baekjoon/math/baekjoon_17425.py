import sys
"""
[풀이]
1) 약수를 뒤집어 생각하면 배수
=> 생각한 것도 맞고, 코드도 거기서 거기인듯 한데 뭐가 도대체 차이가 나는건지 모르겠다.
"""


arr = [1]*10000001
dp = [0]*10000001
T = int(sys.stdin.readline())
for i in range(2, 10000001):
    j = 1
    while i*j <= 10000000:
        arr[i*j] += i
        j += 1
    arr[i] += arr[i-1]
for _ in range(T):
    sys.stdout.write(f"{(arr[int(sys.stdin.readline())])}\n")

