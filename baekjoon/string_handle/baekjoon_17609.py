import sys
from collections import Counter

"""
[시간]
1) 10:40 ~ 11:25

[요약]
1) 유사회문: 한 문자를 삭제하여 회문으로 만들 수 있는 문자열
    => 유사회문인지 아닌지 판단하는 프로그램 작성
2) 주어진 문자열의 길이는 10만, 문자열 개수는 최대 30개
    => 제한 시간이 1초라서 O(n)의 알고리즘을 설계 필요, Counter 사용 불가
[전략]
1) 슬라이딩 윈도우 혹은 무식하게 루프
"""
for _ in range(int(sys.stdin.readline())):
    text = map(str, sys.stdin.readline().rstrip())
    counter = Counter(text)  # O(n), 더 이상 루프 사용 불가

    if text == text[::-1]:
        print(0)
        continue



