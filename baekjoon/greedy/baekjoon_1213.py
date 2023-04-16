import sys
from collections import Counter
"""
[풀이 시간]
1) 20:40 ~ 21:10

[요약]
1) 주어진 문자열 펠린드롬으로 변환
    - 모두 대문자로 이루어진 알파벳, 최대 50글자
    - 팰린드롬: 중간을 기점으로 대칭인 문자열
[전략]
1) 주어진 문자열을 알파벳 단위로 나눈다.
2) 알파벳의 개수를 카운트한다
    2-1) 홀수인 알파벳을 찾아 중간 지점에 배치한다.
    2-2) 홀수인 알파벳이 없다면 절반으로 자른뒤 사전 순으로 배치하고 리스트에 reverse 한 뒤 이어 붙인다.
"""
text_list = [text for text in sys.stdin.readline().rstrip()]
count_list = [[k, v] for k, v in sorted(Counter(text_list).items())] # Counter 객체의 반환이 정렬된 상태가 아니구나....
tmp, middle, checker = '', '', 0

for i in range(len(count_list)):
    if count_list[i][1] % 2 == 1:
        checker += 1
        middle = count_list[i][0]
    if checker >= 2:
        print("I'm Sorry Hansoo")
        exit()
for i in range(len(count_list)):
    tmp += (count_list[i][0] * (count_list[i][1] // 2))
print(tmp + middle + tmp[::-1]) # start-end-step




