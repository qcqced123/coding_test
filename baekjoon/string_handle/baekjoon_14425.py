import sys

"""
[풀이 시간]
1) 16:30 ~ 17:00

[요약]
1) N개의 문자열로 이루어진 집합 S가 주어진다.
    - 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램 작성
[전략]
1) 세트 교차 방식 (시간 효율성 GOOD)
    - 집합 S에 중복 문자열은 없지만, M개의 문자열 속에는 중복 문자열 존재 가능
    - 중복 문자열까지 모두 세어주도록 코드를 작성해야 함
    => 그게 까다로우니까 사전 대조 방식으로 문제를 해결하자
2) 사전 대조 방식 (공간 효율성 GOOD)
"""
N, M = map(int, sys.stdin.readline().split())
result, str_dict = 0, {}
for _ in range(N):
    str_dict[sys.stdin.readline().rstrip()] = True

for _ in range(M):
    str_tmp = sys.stdin.readline().rstrip()
    try:
        if str_dict[str_tmp]:
            result += 1
    except KeyError as e:
        pass
print(result)

