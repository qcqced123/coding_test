import sys

"""
[시간]
1) 22:10 ~ 22:32

[요약]
1) 두 문자열 X와 Y의 차이: X[i] ≠ Y[i]인 i의 개수
    - X=”jimin”, Y=”minji”이면, 둘의 차이는 4
2) A ≤ B, 두 문자열의 길이가 똑같아 지도록 아래 연산 선택
    - A의 앞에 아무 알파벳이나 추가한다.
    - A의 뒤에 아무 알파벳이나 추가한다.
=> A와 B의 길이가 같으면서, A와 B의 차이를 최소로 하는 프로그램
"""

a, b = map(str, sys.stdin.readline().split())
slicer, checker = len(a), len(b) - len(a) + 1

tmp_min = 99999
for i in range(checker):
    count = 0
    tmp_b = b[i:i+slicer]
    for j in range(slicer):
        if a[j] != tmp_b[j]:
            count += 1
    tmp_min = min(tmp_min, count)
print(tmp_min)
