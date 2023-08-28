import sys
from collections import Counter

"""
[시간]
1) 20:00 ~ 20:30

[요약]
1) DNA를 이루는 뉴클레오티드의 첫글자를 따서 표현, 종류는 4가지
    - A, T, G, C
2)  N개의 길이 M인 DNA가 주어지면 Hamming Distance의 합이 가장 작은 DNA S를 구하기
    - Hamming Distance: 각 위치의 뉴클오티드 문자가 다른 것의 개수
    => 자기 자신을 제외한 나머지 모든 원소와 Hamming Distance를 구하고 총합이 가장 작은 아이를 리턴해라
[전략]
1) linear search 하면서 한 개라도 철자가 다른 자리수 세기
    - 해당 자리수의 알파벳: 가장 빈도수가 높은걸로
"""
N, M = map(int, sys.stdin.readline().split())
dna = [sys.stdin.readline().rstrip() for _ in range(N)]
result, char_list = 0, []  # for append char, count

for i in range(M):
    tmp = []
    for j in range(N):
        tmp.append(dna[j][i])
    counter = Counter(tmp)
    rank_counter = sorted(counter.most_common(), key=lambda x: (-x[1], x[0]))  # - 붙인 정렬 조건은 현재 정렬 기준과 반대로
    result += sum(counter.values()) - rank_counter[0][1]  # counting
    char_list.append(rank_counter[0][0])  # append char

print(''.join(char_list))
print(result)
