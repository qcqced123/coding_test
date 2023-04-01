import sys
"""
[풀이 시간]
1) 19:10 ~ 19:50

[요약]
1) 회의실은 1개, 해야 하는 회의는 N개
    - 시작, 끝나는 시간 주어 지면 가능한 회의가 최대가 되도록 스케줄을 짜보자!
    - 하나의 회의가 끝나는 동시에 다른 회의를 시작할 수 있다
[전략]
1) 시간 압박은 없는 문제
2) 가능한 최대 회의 개수를 구하는 문제
    - Greedy, 무엇을 어떻게 정렬할 것인가 고민
    - 빨리 끝나는 강의를 우선 배정하는 것이 최대 개수 늘리기 적합해 보인다
    - 일단 끝나는 시간을 기준으로 오름 차순 정렬을 해보자
"""

meeting_list, end_time = [list(map(int, sys.stdin.readline().split())) for i in range(int(sys.stdin.readline()))], 0
meeting_list.sort(key=lambda x: (x[1], x[0]))
result = 0
for i in range(len(meeting_list)):
    if meeting_list[i][0] >= end_time:
        result += 1
        end_time = meeting_list[i][1]
print(result)

