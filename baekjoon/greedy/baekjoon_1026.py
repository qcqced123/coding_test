import sys
"""
[풀이 시간]
1) 22:20 ~ 22:50

[요약]
1) 길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S
    - S = A[0] × B[0] + ... + A[N-1] × B[N-1]
    - S값이 최소가 되도록 A의 원소를 재배열, B는 재배열 x
[전략]
1) 배열 & 최소값: Greedy
    - 최소값을 구하려면 B 최대값과 A 최소값을 곱해주어야 한다
    - B 배열을 정렬하지 말라고 했지만, 사실 해도 될 것 같다.
"""
N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())), reverse=False)
B = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
result = []
for i in range(N):
    result.append(A[i] * B[i])
print(sum(result))
