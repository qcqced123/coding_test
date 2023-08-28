import sys
from collections import Counter, deque

"""
[시간]
1) 21:30 ~ 22:00

[요약]
1) DNA 문자열: A, C, G, T로만 구성된 문자열
    => DNA 문자열의 일부를 뽑아 비밀번호로 사용
    => 추출 기준은 서로 다른 문자의 개수가 특정 개수 이상 등장해야 함
    => 만들 수 있는 비밀번호 종류, 추출된 위치가 다르면 문자열이 같아도 다른 비밀번호로 취급
[전략]
1) collections.Counter 사용
    - 처음 슬라이딩 부분까지만 계산
"""
S, P = map(int, sys.stdin.readline().split())
dna = sys.stdin.readline().rstrip()
chars = ['A', 'C', 'G', 'T']
result, minimal = 0, {k: v for k, v in zip(chars, list(map(int, sys.stdin.readline().split())))}

counter = Counter(dna[:P])
for i in range(P-1, S):
    if i != P-1:
        counter[dna[i-P]] -= 1
        counter[dna[i]] += 1
    checker = True
    for char in chars:
        if counter[char] < minimal[char]:
            checker = False
            break
    if checker:
        result += 1
print(result)
